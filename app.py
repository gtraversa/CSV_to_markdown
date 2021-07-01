import PySimpleGUI as sg
import webbrowser
import layout
from magic_tool import converter

window = layout.make_window()

while True:
    event,values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
            break
    elif event == '-CONVERT FILE-':
        path = values['-FILE-']
        success, message = converter(path)
        sg.Popup(message)