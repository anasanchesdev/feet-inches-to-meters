import PySimpleGUI as ps

label1 = ps.Text('Enter feet:')
label2 = ps.Text('Enter inches:')
input1 = ps.InputText(key='feet')
input2 = ps.InputText(key='inches')
button = ps.Button('Convert', key='convert_button')
action_text = ps.Text('', key='action_text')

window = ps.Window('Feet Inches to Meters',
                   layout=[
                       [label1],
                       [input1],
                       [label2],
                       [input2],
                       [button, action_text]
                   ])

while True:
    event, values = window.read()

    try:
        feet = float(values['feet'])
        inches = float(values['inches'])

    except ValueError:
        window['action_text'].update(value='You must type a valid number!', text_color='red')
        continue

window.close()
