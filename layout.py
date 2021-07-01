import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import FolderBrowse,ThisRow

def make_window():
    sg.theme('DarkBlack1')
    file_browse = [
        [
            sg.Text("Select File"),
            sg.In(size=(55, 1), key="-FILE-"),
            sg.FileBrowse(button_text = 'File',file_types=(('CSV Files', '*.csv'),)),
            sg.Button(button_text = 'Convert', enable_events=True, key = '-CONVERT FILE-')
        ],
        [
            sg.Text('Created by Gianluca Traversa (RME Intern), Joe Rush and Jessica Lucas © 2021.',
            tooltip='Source Code',
            enable_events = True,
            font = ('Helvetica',7),
            text_color='Gray',
            key = '-COPYRIGHT-'),
        ]
    ]
    layout = [file_browse]
    return sg.Window('CSV Converter',layout,finalize = True, icon = r'C:\Users\gttraver\Desktop\Magic tool\Logo\logo_icon.ico')