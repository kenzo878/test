from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout

import json
app = QApplication([])

#membuat jendela utama
notes_win = QWidget()
notes_win.setWindowTitle('Smart Notes')
notes_win.resize(900, 600)

#tombol dan lainnya
list_notes = QListWidget()
list_notes_label = QLabel('Daftar Notes')

button_note_create = QPushButton('Buat note')
button_note_delete = QPushButton('Hapus note')
button_note_save = QPushButton('Simpan note')

field_tag = QLineEdit('')
field_tag.setPlaceholderText('Masukkan tag...')
field_text = QTextEdit()
button_add = QPushButton('Masukkan ke note')
button_del = QPushButton('Hilangkan dari note')
button_search = QPushButton('Cari notes menggunakan tag')
list_tags = QListWidget()
list_tags_label = QLabel('Daftar dari tag')

#menaruh widget pada tempatnya
layout_notes= QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)

col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)

row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_delete)

row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)

col_2.addLayout(row_1)
col_2.addLayout(row_2)
col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)

row_3 = QHBoxLayout()
row_3.addWidget(button_add)
row_3.addWidget(button_del)

row_4 = QHBoxLayout()
row_4.addWidget(button_search)

col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout_notes.addLayout(col_1, stretch = 2)
layout_notes.addLayout(col_2, stretch = 1)
notes_win.setLayout(layout_notes)

def show_note():
    #get the text from the note with the title highlighted and display it in the edit field
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_text.setText(notes[key]["text"])
    list_tags.clear()
    list_tags.addItems(notes[key]["tags"])

#connecting event handling
list_notes.itemClicked.connect(show_note)

#run the application 
notes_win.show()

with open("notes_data.json", "r") as file:
    notes = json.load(file)
list_notes.addItems(notes)

app.exec_()