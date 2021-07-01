import PySimpleGUI as sg
import webbrowser
import layout
from magic_tool import converter

""" GUI for .csv to Markdown converter

    Created by Gianluca Traversa (RME Intern) © 2021.
    https://github.com/gtraversa/AmazonRME
    gianlu.traversa@gmail.com
    
    Amazon EMA1, Derbishire, UK.
"""

window = layout.make_window()

while True:
    event,values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
            break
    elif event == '-CONVERT FILE-':
        path = values['-FILE-']
        success, message = converter(path)
        if success:
            title = 'Success'
        else:
            title = 'Error'
        sg.Popup(message, title = title, icon = r'C:\Users\gttraver\Desktop\Magic tool\Logo\logo_icon.ico')
    elif event == '-COPYRIGHT-':
            url = 'https://github.com/gtraversa/CSV_to_markdown'
            webbrowser.open(url, new=0, autoraise=True)