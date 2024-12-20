import maya.cmds as cmds
import json
import os
import sys
sys.path.append("C:\ILLOGIC_APP\Prism\2.0.11\app\Plugins\Apps\PluginEmpty\Integration")
import PrismInit
core=PrismInit.pcore

def read_shotInfo(jsonPath,seqID,shID):
    with open(jsonPath, 'r') as file:
        data = json.load(file)

    result = {}
    entities = data.get("shots", {}).get(seqID, {}).get(shID, {}).get("connectedEntities", [])
    if entities :
        print(entities)
        for entity in data["shots"][seqID][shID]["connectedEntities"]:
            asset_path_parts = entity["asset_path"].split("\\")
            if len(asset_path_parts) == 2:
                asset_name, asset_directory = asset_path_parts[1], asset_path_parts[0]
                result[asset_name] = asset_directory
        return result
    else: 
        errorMessage=f"{seqID}_{shID} has no entities connected"
        print(errorMessage)
        show_error_window(errorMessage,250,275)

def get_curent_shotKey():
    scene_path = cmds.file(query=True, sceneName=True)
    file_name_with_extension = os.path.basename(scene_path)
    file_name = os.path.splitext(file_name_with_extension)[0]
    shotKey=file_name = file_name.split("_")[0]
    try:
        seqID,shID=shotKey.split("-")
    except Exception as error:
        seqID,shID=None,None
    return seqID,shID

def show_error_window(errorMessage,width,height):
    if cmds.window("errorWindow", exists=True):
        cmds.deleteUI("errorWindow", window=True)
    window = cmds.window("errorWindow", title="Error", widthHeight=(width,height))
    cmds.columnLayout(adjustableColumn=True)
    cmds.text(label="", align='center')
    cmds.text(label=errorMessage, align='center')
    cmds.text(label="", align='center')
    cmds.button(label="OK", command=('cmds.deleteUI(\"' + window + '\", window=True)'))
    cmds.showWindow(window)

def import_rig(asset,type):
    print(f"importing the rig of the {type}, {asset}")
    sucessFullReportMessages.append(f"{type} {asset}")

def import_usd(asset,type):
    print(f"importing the usd of the {type}, {asset}")
    sucessFullReportMessages.append(f"{type} {asset}")

def report(sucessFullReportMessages,faillureReportMessages):
    if cmds.window("reportWindow", exists=True):
        cmds.deleteUI("reportWindow", window=True)
    window = cmds.window("reportWindow", title="report", widthHeight=(300, 500))
    cmds.columnLayout(adjustableColumn=True)
    cmds.text(label="", align='center')

    if sucessFullReportMessages:
        cmds.text(label="", align='center')
        cmds.text(label="succesfully imported :", align='center')
        cmds.text(label="", align='center')
        for sucessFullReportMessage in sucessFullReportMessages:
            cmds.text(label=sucessFullReportMessage, align='center')
        cmds.text(label="", align='center')

    if faillureReportMessages:
        cmds.text(label="", align='center')
        cmds.text(label="failed import :", align='center')
        cmds.text(label="", align='center')
        for faillureReportMessage in faillureReportMessages:
            cmds.text(label=faillureReportMessage, align='center')
        cmds.text(label="", align='center')
    
    cmds.text(label="", align='center')
    cmds.button(label="OK", command=('cmds.deleteUI(\"' + window + '\", window=True)'))
    cmds.showWindow(window)

def print_current_project_name():
    current_project = core.get_current_project()
    if current_project:
        print(f"Current Project Name: {current_project.name}")
    else:
        print("No current project found.")

animableList=["Characters","Character","Chara","characters","character","chara","props","prop","Props","Prop"]
shotInfoJson=r"I:\swaChristmas_2407\00_Pipeline\Shotinfo\shotInfo.json"
sucessFullReportMessages=[]
faillureReportMessages=[]

seqID,shID=get_curent_shotKey()
print_current_project_name()

if seqID and shID:
    shotEntites=read_shotInfo(shotInfoJson,seqID,shID)
    print(shotEntites)
    for asset, type in shotEntites.items():
        if type in animableList:
            print(f"{asset} is animable")
            import_rig(asset,type)
        else:
            print(f"{asset} is not animable")
            import_usd(asset,type)
    report(sucessFullReportMessages,faillureReportMessages)
else:
    show_error_window('''cannot read in which sequence or shot is your scene
    are you sure that your scene is in the pipe?
    do your scene follow the naming rule:
    SEQUENCE-SHOT_Anim_v###.ma ?''',300,120)