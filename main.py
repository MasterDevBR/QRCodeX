import PySimpleGUI as sg
import qrcode

sg.theme('DarkBlue')

layout = [
    [sg.Text(f'QRcodeX', size=(25,1), justification='center', font=('Helvetica', 14))],
    [sg.Text('Link', font=('Helvetica', 10)), sg.InputText(key='input', size=(35,1), justification='r', font=('Lucida faz', 10))],
    [sg.Button('Gerar', font=('Helvetica', 10), size=(17,3), button_color=('black', 'light blue')), sg.Button('Fechar', font=('Britannic', 10), size=(17,3), button_color=('black', 'light blue'))],
    [sg.Image(r'C:\Users\Junio\PycharmProjects\QRCODE_Generator\Images\qrcreated.PNG', key=2, size=(290, 300))]

]
window = sg.Window('QRcodeX - Gerador de QRCode', layout, grab_anywhere=True, alpha_channel=0.9)



while True:

    event, values = window.Read()

    if event == 'Fechar':
        window.close()
    elif event == 'Gerar':
        values_on_input = (values['input'])
        img = qrcode.make(values_on_input,border=0, version=1)
        img.save(f'qrcreated.PNG')
        print(values_on_input)
    window[2].Update(f'qrcreated.PNG')


