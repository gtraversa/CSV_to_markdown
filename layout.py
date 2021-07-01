import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import FolderBrowse,ThisRow

def make_window():
    file_browse = [
        [
            sg.Text("Select File"),
            sg.In(size=(55, 1), key="-FILE-"),
            sg.FileBrowse(button_text = 'File',file_types=(('CSV Files', '*.csv'),)),
            sg.Button(button_text = 'Convert', enable_events=True, key = '-CONVERT FILE-')
        ],
    ]
    layout = [file_browse]
    return sg.Window('CSV Converter',layout,finalize = True)