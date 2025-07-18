import FreeSimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select a file to compress:")
input_box1 = sg.InputText()
choose_button1 = sg.FilesBrowse("Choose", key="Files",)
label2 = sg.Text("Select a destination :")
input_box2 = sg.InputText()
choose_button2 = sg.FolderBrowse("Choose", key="Folder")
compress_Button = sg.Button("Compress")
output = sg.Text("Output will be shown here", key="Output" , text_color="red")

window = sg.Window("File Compression Tool",
                   layout=[[label1, input_box1, choose_button1],
                           [label2, input_box2, choose_button2],
                           [compress_Button , output]])

while True :
    event, values = window.read()
    print(event, values)
    filepaths = values["Files"].split(";")
    folder = values["Folder"]
    make_archive(filepaths, folder)
    window["Output"].update("Files compressed successfully!")



window.close()