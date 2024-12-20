import maya.cmds as cmds
import json
import os
import sys
import PrismInit
core=PrismInit.pcore
from qtpy.QtWidgets import *

"""
ce script importe automatiquement les rig ou les usd des connected entities en fonction de si c'est un asset animable ou non

par example ce script va importer les rigs des characters et props en references en reference mais les USD des sets et enviro en reference

limitation:
1 sont concidéré comme animable la list :"animableList" cette liste doit etre mise a jour si d'autre category d'asset voit le jour
2 pour etre detecté en tant que rig, le product de ce dernier doit s'appeler comme "animableProductName" si la nomenclature du publish de rig change il faut mettre a jour ce script

"""

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

def create_importList(shotEntites):
    importList = []
    faillureReportMessages=[]
    for entity in shotEntites:
        print(entity)
        products = core.products.getProductsFromEntity(entity)
        asset_path_parts = entity["asset_path"].split("\\")
        assetType=asset_path_parts[0]

        if assetType in animableList:
            productName=animableProductName
        else:
            productName=staticProductName

        selectedProduct = [asset for asset in products if asset['product'] == productName]
        if not selectedProduct:
            existingProduct=[]
            for asset in products: existingProduct.append(asset['product'])
            faillureReportMessages.append(f"can't import {asset_path_parts[1]}, there is no {productName} product for it there is only : {existingProduct}")
        importList += selectedProduct
    return importList ,faillureReportMessages

def sort_object(object):
    if not cmds.objExists('world'):
        print("No 'world' object found. Creating a new hierarchy...")
        world_node = cmds.group(em=True, name='world')

        cmds.group(em=True, name='assets', parent=world_node)
        cmds.group(em=True, name='characters', parent=world_node)
        cmds.group(em=True, name='props', parent=world_node)
        cmds.group(em=True, name='environnement', parent=world_node)
    else:
        print("'world' object already exists in the scene.")
    print(object)



animableList=["Characters","Character","Chara","characters","character","chara","props","prop","Props","Prop"]

sucessFullReportMessages=[]
#settings
animableProductName='Rigging_forAnim'
staticProductName='USD'

fileName = core.getCurrentFileName()
currentEntity = core.getScenefileData(fileName)
shotEntites=core.entities.getConnectedEntities(currentEntity)

importList,faillureReportMessages=create_importList(shotEntites)

for _, product in enumerate(importList):
    path = core.products.getLatestVersionpathFromProduct(product["product"], entity=product)
    object=core.getStateManager().importFile(path,activateWindow=False)
    sort_object(object)

if faillureReportMessages:
    report(sucessFullReportMessages,faillureReportMessages)
