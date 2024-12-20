import maya.cmds as cmds
import json
import os
import sys
import PrismInit
core=PrismInit.pcore
from qtpy.QtWidgets import *



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

def createImportList(shotEntites):
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

animableList=["Characters","Character","Chara","characters","character","chara","props","prop","Props","Prop"]
sm = core.getStateManager()
sucessFullReportMessages=[]
#settings
animableProductName='Rigging_forAnim'
staticProductName='USD'

fileName = core.getCurrentFileName()
currentEntity = core.getScenefileData(fileName)
shotEntites=core.entities.getConnectedEntities(currentEntity)

importList,faillureReportMessages=createImportList(shotEntites)
report(sucessFullReportMessages,faillureReportMessages)

for _, product in enumerate(importList):
    path = core.products.getLatestVersionpathFromProduct(product["product"], entity=product)
    sm.importFile(path,activateWindow=False)
