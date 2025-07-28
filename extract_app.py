import FreeSimpleGUI as sg
import zipfile
import extractor
from Products.Extract_GUI.extractor import archive_extract

sg.theme("black")
label1 = sg.Text("Select Archive: ")
input1 = sg.InputText(tooltip="Add Archive")
button1 = sg.FilesBrowse("Choose",key="archive")

label2 = sg.Text("Select Dest Dir:")
input2 = sg.InputText(tooltip="Add Destination")
button2 = sg.FolderBrowse("Choose",key="dest_dir")

button3 = sg.Button("Extract",key="extract")
error = sg.Text(text_color="red",key="error")
output = sg.Text(text_color="green",key="output")

window = sg.Window("Archive Extractor",
                   layout=[[label1,input1,button1],
                           [label2,input2,button2],
                           [button3,error,output]])

while True:
    event, values = window.read()
    match event:
        case sg.WIN_CLOSED:
            break
        case "extract":
            list_paths = values["archive"].split(';')
            dest_path = values["dest_dir"]
            for file_path in list_paths:
                archive_extract(file_path, dest_path)
            window["error"].update("")
            window["output"].update("Extraction completed!")

window.close()