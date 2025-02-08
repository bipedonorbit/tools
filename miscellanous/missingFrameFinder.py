import cv2
import os
import json
import sys
from PySide6.QtWidgets import *
import matplotlib.pyplot as plt

RED = "\033[31m"
BLUE = "\033[34m"
YELLOW = "\033[33m"
RESET = "\033[0m"

def getFrameRange(seqID,shID):
            shotName=seqID+"_"+shID
            with open(r"\\MINERVA\3d4_23_24\MECHA\02_ressource\@LOUIS\ressources\thumbnail\timeRanges.json", 'r') as file:
                data = json.load(file)
            if shotName in data:
                values = data[shotName]
                
                return (values)

exrPath="\\MINERVA\3d4_23_24\MECHA\08_editing\input\05_render"

def getShotList():
    shotList=[]
    with open(r"\\MINERVA\3d4_23_24\MECHA\02_ressource\@LOUIS\ressources\thumbnail\timeRanges.json", 'r') as file:
        data = json.load(file)
    for shotName in data:
        shotList.append(shotName)
    return shotList

def getFrames(path,index):
    frameList=os.listdir(path)
    frameNumberList=[]
    for frame in frameList:
        splittedFrame=frame.split('_')
        frameNumber=splittedFrame[index]
        root, ext = os.path.splitext(frameNumber)
        frameNumberList.append(root)
    return frameNumberList

def convertFrameRangeToFrameList(frameRange):
    start, end = frameRange
    FrameList = [i for i in range(start, end + 1)]
    formatted_frames = [f'{frame:04d}' for frame in FrameList]
    return formatted_frames

shotList=getShotList()
shotList.remove("carton")
task_status = {shotList[i]: {"RL": "todo", "OUT": "todo"} for i in range(len(shotList))}
specialShot=["seq010_sh206","seq010_sh180"]
for shot in specialShot:
    task_status[shot]["RL"]="done"
    task_status[shot]["OUT"]="done"


#shotList=["seq010_sh010"]
for shot in shotList:
    SEQID,SHID=shot.split('_')
    RLinputPath=f"//MINERVA/3d4_23_24\MECHA/08_editing/input/05_render/{SEQID}/{SHID}/publish"
    compoOutputPath=f"//MINERVA/3d4_23_24\MECHA/08_editing/input/06_compo/{SEQID}/{SHID}/MCH_{SEQID}_{SHID}_exr/"

    try:
        rlList=os.listdir(RLinputPath)
        filtered_rlList = [file for file in rlList if not file.endswith('.txt')]
        frameRange=getFrameRange(SEQID,SHID)
        goalFrameList=convertFrameRangeToFrameList(frameRange)
        goalFrameList = set(goalFrameList)
        for RL in filtered_rlList:
            rlSequencePath=os.path.join(RLinputPath,RL)
            RlframeList=getFrames(rlSequencePath,5)
            # Convert lists to sets
            RlframeList = set(RlframeList)
            missing_frames = goalFrameList - RlframeList
            missing_frames = sorted(list(missing_frames))
            if missing_frames:
                missing_frames = ','.join(missing_frames)
                print(f"{RED}there is missing frames in {shot} in the renderlayer {RL}: {RESET}")
                print(missing_frames)
            else :
                print(f"{BLUE}no missing frames in {shot} in the renderlayer {RL}: {RESET}")
                task_status[shot]["RL"]="done"
        try:
            compoOutputSequence=getFrames(compoOutputPath,3)
            compoOutputSequence = set(compoOutputSequence)
            
            missing_frames = goalFrameList - compoOutputSequence
            if missing_frames:
                #missing_frames = ','.join(missing_frames)
                missing_frames = sorted(list(missing_frames))
                print(" ")
                print(f"{RED}there is missing frames in {shot} compo output: {RESET}")
                print(missing_frames)
                print("")
            else :
                print("")
                print(f"{YELLOW}no missing frames for {shot} in compo output {RESET}")
                print("")
                task_status[shot]["OUT"]="done"

        except Exception as e:
             print("")
             print(f"{RED}can't list dir in compo output on {shot} it might not exist{RESET}")
             print("")

    except Exception as e:
         print(f"can't list dir in for {shot}")
         print(e)

for key, statuses  in task_status.items():
    if statuses['RL'] == "todo":   
        print(f"{RED}{key} RL {statuses['RL']}{RESET}")
    else:
        print(f"{YELLOW}{key} RL {statuses['RL']}{RESET}")
    if statuses['OUT'] == "todo":
        print(f"{RED}{key} OUT {statuses['OUT']}{RESET}")
    else:
        print(f"{YELLOW}{key} OUT {statuses['OUT']}{RESET}")
