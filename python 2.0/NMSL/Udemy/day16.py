import PySimpleGUI as sg

feet_label = sg.Text("Enter feet: ")
inches_label = sg.Text("Enter inches: ")
feet = sg.Input()
inches = sg.Input()
convert_button = sg.Button("Convert")

window = sg.Window("Convertor", 
                   layout=[[feet_label,feet],
                           [inches_label,inches],[convert_button]])

window.read()
window.close()