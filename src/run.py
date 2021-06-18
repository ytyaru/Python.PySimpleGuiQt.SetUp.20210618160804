#!/usr/bin/env python3
# coding: utf8
#import PySimpleGUIWeb as sg
#import PySimpleGUIWx as sg
#import PySimpleGUI as sg
import PySimpleGUIQt as sg

print(dir(sg))
print(sg.theme_list())

sg.theme('DarkGreen')

layout = [
    [sg.Text('PySimpleGUIWeb テスト')],
    [sg.Text('名前', size=(15, 1)), sg.InputText('山田太郎')],
    [sg.Text('年齢', size=(15, 1)), sg.Spin(None, initial_value=20)],
    [sg.Text('趣味', size=(15, 1)), sg.Combo(['料理','読書','映画'])],
    [sg.Submit(button_text='実行')]
]

window = sg.Window('PySimpleGUIWeb テスト', layout)

while True:
    event, values = window.read()
    if event is None:
        print('exit')
        break
    if event == '実行':
        show_message = "名前：" + values[0] + '\n'
        show_message += "年齢：" + values[1] + '\n'
        show_message += "趣味：" + values[2] + 'が入力されました。'
        print(show_message)
        sg.popup(show_message)

window.close()

