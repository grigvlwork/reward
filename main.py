import sys
import traceback
import subprocess
import pyperclip
import black
import sys
import re
import enchant
import difflib
import datetime
import time
import shutil
import os
import glob
import qdarkstyle
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
from PyQt5 import QtGui
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from mainwindow import Ui_MainWindow
import requests


def remove_comments(code):
    return re.sub(r'#.*', '', code)


def run_text(text, timeout):
    with open('code.py', 'w', encoding='utf-8') as c:
        c.write(text)
    try:
        completed_process = subprocess.run(['python', 'code.py'], capture_output=True, text=True, timeout=timeout)
        if completed_process.returncode == 0:
            t = completed_process.stdout
            t = t.encode('cp1251').decode('utf-8')
            if len(t) > 50:
                return t[:50] + '..'
            else:
                return t
        else:
            t = completed_process.stderr
            t = t.encode('cp1251').decode('utf-8')
            # if len(t) > 50:
            #     return t[:150] + '\n' + t[150:]
            # else:
            return t
    except subprocess.TimeoutExpired:
        return f'Программа выполнялась более {timeout} секунд'


def spell_check(text):
    rus_alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    words = []
    word = ''
    for c in text:
        if c.lower() in rus_alph:
            word += c
        else:
            if len(word) > 0:
                words.append(word)
                word = ''
    result = []
    dictionary = enchant.Dict("ru_RU")
    for w in words:
        if not dictionary.check(w):
            sim = dict()
            suggestions = set(dictionary.suggest(w))
            for word in suggestions:
                measure = difflib.SequenceMatcher(None, w, word).ratio()
                sim[measure] = word
            result.append([w, sim[max(sim.keys())]])
    return result


def check_dict():
    file1 = '/_venv/Lib/site-packages/enchant/data/mingw64/share/enchant/hunspell/ru_RU.aff'
    file2 = '/_venv/Lib/site-packages/enchant/data/mingw64/share/enchant/hunspell/ru_RU.dic'
    file_path1 = os.getcwd() + '/venv/Lib/site-packages/enchant/data/mingw64/share/enchant/hunspell/ru_RU.aff'
    file_path2 = os.getcwd() + '/venv/Lib/site-packages/enchant/data/mingw64/share/enchant/hunspell/ru_RU.dic'
    file_path = os.getcwd() + '/venv/Lib/site-packages/enchant/data/mingw64/share/enchant/hunspell/'
    try:
        if (not os.path.exists(file_path1)) or (not os.path.exists(file_path2)):
            for file in glob.glob(os.getcwd() + file1):
                shutil.copy(file, file_path)
            for file in glob.glob(os.getcwd() + file2):
                shutil.copy(file, file_path)
        return True
    except Exception:
        return False


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.explanation_text = ''
        self.answer_number = 0
        self.rb0.setChecked(True)
        self.allow_spell_check = check_dict()
        self.correct_code_model = QStandardItemModel()
        self.explanation_pte.textChanged.connect(self.explanation_changed)
        self.run_btn.clicked.connect(self.run_correct)
        self.rb0.clicked.connect(self.answer_number_change)
        self.rb1.clicked.connect(self.answer_number_change)
        self.rb2.clicked.connect(self.answer_number_change)
        self.toggle_theme_btn.clicked.connect(self.change_theme)
        self.pep8_btn.clicked.connect(self.pep8_correct)
        self.paste_btn.clicked.connect(self.paste_code)
        self.paste_explanation_btn.clicked.connect(self.paste_explanation)
        self.correct_tw.currentChanged.connect(self.correct_row_generator)
        self.setWindowTitle(f'Проверка реворд {self.check_version()}')

    def check_version(self):
        v = None
        try:
            with open('version.txt') as f:
                v = f.read().strip()
        except Exception as e:
            print(str(e))
        if v is not None:
            try:
                r = requests.get('https://github.com/grigvlwork/reward/blob/master/version.txt')
                new_v = r.text[r.text.find("rawLines") + 12:r.text.find("rawLines") + 17]
                if v != new_v:
                    QMessageBox.information(self,
                                            'Информация', f'Вышла новая версия {new_v}\nОбновите программу',
                                            QMessageBox.Ok)
            except Exception as e:
                print(str(e))
            return v
        return ''

    def change_theme(self):
        if self.toggle_theme_btn.text() == 'Светлая тема':
            self.toggle_theme_btn.setText('Тёмная тема')
            app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=qdarkstyle.LightPalette))
        else:
            self.toggle_theme_btn.setText('Светлая тема')
            app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=qdarkstyle.DarkPalette))

    def run_correct(self):
        file_names = ['9.txt', '9.csv', '17.txt', '22.txt', '24.txt', '26.txt', '27_A.txt', '27_B.txt']
        code = self.correct_code_pte.toPlainText()
        file_name = self.number_cb.currentText() + '.*'
        use_file = False
        for file in file_names:
            if file in code:
                file_name = file
                use_file = True
                break
        if (self.part_cb.currentText() == 'beta' or
                self.number_cb.currentText() in ['17', '22', '24']):
            folder = '/files/beta/'
        else:
            folder = '/files/' + self.part_cb.currentText() + '/'
        if use_file:
            try:
                for file in glob.glob(os.getcwd() + folder + file_name):
                    shutil.copy(file, os.getcwd())
            except Exception:
                self.correct_output_lb.setText('Файл не найден')
                return
        code = self.correct_code_pte.toPlainText()
        timeout = self.timeout_sb.value()
        self.correct_output_lb.setText('Вывод: ' + run_text(remove_comments(code), timeout))
        if use_file:
            try:
                for file in glob.glob(os.getcwd() + '/' + file_name):
                    os.remove(file)
            except Exception:
                pass

    def get_answer_number(self):
        if self.rb0.isChecked():
            return 0
        elif self.rb1.isChecked():
            return 1
        return 2

    def explanation_changed(self):
        self.explanation_text = self.explanation_pte.toPlainText()
        self.answer_number = self.get_answer_number()
        self.set_my_answer()

    def pep8_correct(self):
        self.correct_code_pte.setPlainText(self.correct_code_pte.toPlainText().replace('\t', '    '))
        code = self.correct_code_pte.toPlainText()
        try:
            code = black.format_str(code, mode=black.Mode(
                target_versions={black.TargetVersion.PY310},
                line_length=101,
                string_normalization=False,
                is_pyi=False,
            ), )
        except Exception as err:
            code = code.strip()
        self.correct_code_pte.setPlainText(code)
        self.correct_code = code

    def copy_my_answer(self):
        pyperclip.copy(self.my_answer_pte.toPlainText())

    def correct_row_generator(self):
        if self.correct_tw.currentIndex() == 1:
            self.correct_code_model.clear()
            for row in self.correct_code_pte.toPlainText().split('\n'):
                it = QStandardItem(row)
                self.correct_code_model.appendRow(it)
            self.correct_code_tv.setModel(self.correct_code_model)
            self.correct_code_tv.horizontalHeader().setVisible(False)
            self.correct_code_tv.resizeColumnToContents(0)

    def paste_code(self):
        self.correct_code_pte.clear()
        self.correct_code_pte.appendPlainText(pyperclip.paste())

    def paste_explanation(self):
        self.explanation_pte.clear()
        self.answer_number = 0
        self.explanation_pte.appendPlainText(pyperclip.paste())
        self.rb0.setChecked(True)

    def answer_number_change(self):
        self.answer_number = int(self.sender().text())
        self.set_my_answer()

    def set_my_answer(self):
        self.my_answer_pte.setPlainText(str(self.answer_number) + '\n<comment>\n' + self.explanation_text +
                                        '\n<comment>')


def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print(tb)
    msg = QMessageBox.critical(
        None,
        "Error catched!:",
        tb
    )
    QApplication.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.excepthook = excepthook
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=qdarkstyle.DarkPalette))
    ex.show()
    sys.exit(app.exec_())
