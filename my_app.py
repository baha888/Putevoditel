from PyQt5 import Qt
from PyQt5.QtWidgets import QPushButton, QApplication, QWidget, QListWidget, QTextEdit, QLineEdit, QHBoxLayout, QVBoxLayout
import json

app = QApplication([])
window = QWidget()
window.setWindowTitle('Путеводитель')

list_countries = QListWidget()
text_countries = QTextEdit()
name_countries = QLineEdit()
name_countries.setPlaceholderText('Введите страну...')
add_country_button = QPushButton('Добавить страну')
del_country_button = QPushButton('Удалить страну')
edit_country_button = QPushButton('Изменить страну')

main_layout = QHBoxLayout()
left_layout = QVBoxLayout()
right_layout = QVBoxLayout()
layout_buttons = QHBoxLayout()

layout_buttons.addWidget(add_country_button)
layout_buttons.addWidget(del_country_button)
layout_buttons.addWidget(edit_country_button)

left_layout.addWidget(list_countries)
right_layout.addWidget(text_countries)
right_layout.addWidget(name_countries)
right_layout.addLayout(layout_buttons)

main_layout.addLayout(left_layout, 3)
main_layout.addLayout(right_layout, 7)


window.setLayout(main_layout)

countries = {
    'fds': ''
}
with open('countries.json', 'w', encoding='utf-8') as file:
        json.dump(countries, file)

def fill_countries():
    list_countries .clear()
    with open('countries.json', 'r', encoding='utf-8') as file:
        countries = json.load(file)
    for country in countries:
        list_countries.addItem(country)

fill_countries()

def clear_widgets():
    text_countries.clear()
    name_countries.clear()

def info_country():
    country = list_countries.selectedItems()[0].text()
    with open('countries.json', 'r', encoding='utf-8') as file:
        countries = json.load(file)
    text_countries.setText(countries[country])

def add_country():
    country = name_countries.text()
    with open('countries.json', 'r', encoding='utf-8') as file:
        countries = json.load(file)
    if not(country in countries):
        countries[country] = ''
    with open('countries.json', 'w', encoding='utf-8') as file:
        json.dump(countries, file)
    fill_countries()
    clear_widgets()

def del_country():
    if list_countries.selectedItems():
        country = list_countries.selectedItems()[0].text()
        with open('countries.json', 'r', encoding='utf-8') as file:
            countries = json.load(file)
        del countries[country]
        with open('countries.json', 'w', encoding='utf-8') as file:
            json.dump(countries, file)
        fill_countries()
        clear_widgets()

def edit_country():
    if list_countries.selectedItems():
        country = list_countries.selectedItems()[0].text()
        with open('countries.json', 'r', encoding='utf-8') as file:
            countries = json.load(file)
        text_country = text_countries.toPlainText()
        countries[country] = text_country
        with open('countries.json', 'w', encoding='utf-8') as file:
            json.dump(countries, file)
        text_countries.clear()
        clear_widgets()

window.setStyleSheet("background-color: grey")
list_countries.setStyleSheet("border: 2px solid white; font-size: 24px; color: white; font-size: italic; font-family: georgia")
text_countries.setStyleSheet("border: 2px solid white; font-size: 24px; color: white; font-size: italic; font-family: georgia")
name_countries.setStyleSheet("border: 2px solid white; font-size: 24px; color: white; font-size: italic; font-family: georgia")
add_country_button.setStyleSheet("border: 2px solid white; font-size: 20px; color: white; font-size: italic; font-family: georgia")
del_country_button.setStyleSheet("border: 2px solid white; font-size: 20px; color: white; font-size: italic; font-family: georgia")
edit_country_button.setStyleSheet("border: 2px solid white; font-size: 20px; color: white; font-size: italic; font-family: georgia")


add_country_button.clicked.connect(add_country)
del_country_button.clicked.connect(del_country)
edit_country_button.clicked.connect(edit_country)
list_countries.itemClicked.connect(info_country)

window.show()
app.exec()








