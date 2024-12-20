import maya.cmds as cmds
import json
import os
import sys
import PrismInit
core=PrismInit.pcore
from qtpy.QtWidgets import *

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
    sm = core.getStateManager()
    with core.waitPopup(core, "Gathering rig...") as popup:
        productsToImport = []

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


animableList=["Characters","Character","Chara","characters","character","chara","props","prop","Props","Prop"]
shotInfoJson=r"I:\swaChristmas_2407\00_Pipeline\Shotinfo\shotInfo.json"
sucessFullReportMessages=[]
faillureReportMessages=[]
productsToImport = []
productName='Rigging_forAnim'

sm = core.getStateManager()

fileName = core.getCurrentFileName()
currentEntity = core.getScenefileData(fileName)
shotEntites=core.entities.getConnectedEntities(currentEntity)

for entity in shotEntites:
    with core.waitPopup(core, "Gathering products...") as popup:
        products = core.products.getProductsFromEntity(entity)
        selectedProduct = [asset for asset in products if asset['product'] == productName]
        productsToImport += selectedProduct

for idx, product in enumerate(productsToImport):

    if "asset_path" not in product:
        continue

    # update popup text
    text = "Importing %s (%s/%s)" % (product["asset_path"], idx+1, len(productsToImport))
    popup.msg.setText(text)
    QApplication.processEvents()
    path = core.products.getLatestVersionpathFromProduct(product["product"], entity=product)
    sm.importFile(path,activateWindow=None)


