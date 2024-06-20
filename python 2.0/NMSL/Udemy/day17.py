import PySimpleGUI as sg

sg.theme("Black")
feet_label = sg.Text("Enter feet: ")
inches_label = sg.Text("Enter inches: ")
feet = sg.Input(key="feet")
inches = sg.Input(key="inches")
convert_button = sg.Button("Convert")
answer = sg.Text(key="answer")
exit_button = sg.Button("Exit")

window = sg.Window("Convertor", 
                   layout=[[feet_label,feet],
                           [inches_label,inches],
                           [convert_button,exit_button,answer]])

while True:
    event, values = window.read()
    
    match event:
        case "Convert":
            answer = float(values['feet'])/3.281 + float(values['inches'])/39.37
            window["answer"].update(value=f'{answer:.2f} m')
        case "Exit":
            break

# import PySimpleGUI as sg
 
 
# def km_to_miles(km):
#     return km / 1.6
 
# sg.theme("Black")
# label = sg.Text("Kilometers: ")
# input_box = sg.InputText(tooltip="Enter todo", key="kms")
# miles_button = sg.Button("Convert")
# output = sg.Text(key="output")
# exit_button = sg.Button("Exit")
 
# window = sg.Window('Km to Miles Converter',
#                    layout=[[label, input_box], [miles_button, output,exit_button]],
#                    font=('Helvetica', 10))
 
# while True:
#     event, values = window.read()
#     match event:
#         case "Convert":
#             km = int(values["kms"])
#             result = km_to_miles(km)
#             window['output'].update(value=result)
#         case "exit_button":
#             break
#         case sg.WIN_CLOSED:
#             break
 
# window.close()