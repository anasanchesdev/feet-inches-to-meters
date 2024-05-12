import PySimpleGUI as ps

ps.theme('Dark')
label1 = ps.Text('Enter feet:')
label2 = ps.Text('Enter inches:')
input1 = ps.InputText(key='feet')
input2 = ps.InputText(key='inches')
button = ps.Button('Convert', key='convert_button')
exit_button = ps.Button('Exit', key='exit_button')
action_text = ps.Text('', key='action_text')

window = ps.Window('Feet Inches to Meters',
                   layout=[
                       [label1],
                       [input1],
                       [label2],
                       [input2],
                       [button, exit_button, action_text]
                   ])

while True:
    event, values = window.read()

    if event == 'exit_button' or event == ps.WIN_CLOSED:
        break

    try:
        feet = float(values['feet'])
        inches = float(values['inches'])

    except ValueError:
        window['action_text'].update(value='You must type a valid number!', text_color='red')
        continue

    meters = feet * 0.3048 + inches * 0.0254
    window['action_text'].update(value=f'{meters:.4f}m', text_color='white', font='Arial')

window.close()
