import FreeSimpleGUI as sg

label1 = sg.Text("Select a file to compress:")
input_box1 = sg.InputText()
choose_button1 = sg.FilesBrowse("Choose File")
label2 = sg.Text("Select a destination :")
input_box2 = sg.InputText()
choose_button2 = sg.FolderBrowse("Choose Destination")
compress_Button = sg.Button("Compress")


window = sg.Window("File Compression Tool",
                   layout=[[label1, input_box1, choose_button1],
                           [label2, input_box2, choose_button2],
                           [compress_Button]])

window.read()
window.close()