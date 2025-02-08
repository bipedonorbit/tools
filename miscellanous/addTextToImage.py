import cv2
import os
import json

def resize_image(image, width=None, height=None):
    # Calculate the new dimensions
    if width is None and height is None:
        return image
    elif width is None:
        aspect_ratio = height / float(image.shape[0])
        new_width = int(image.shape[1] * aspect_ratio)
        new_height = height
    elif height is None:
        aspect_ratio = width / float(image.shape[1])
        new_width = width
        new_height = int(image.shape[0] * aspect_ratio)
    else:
        new_width = width
        new_height = height

    # Resize the image
    resized_image = cv2.resize(image, (new_width, new_height))

    return resized_image

def high_lighted_text(image,text,x,y,font_scale, width, height):


    # Draw the black border
    if width is None and height is None:
        return image
    elif width is None:
        aspect_ratio = height / float(image.shape[0])
        new_width = int(image.shape[1] * aspect_ratio)
        new_height = height
    elif height is None:
        aspect_ratio = width / float(image.shape[1])
        new_width = width
        new_height = int(image.shape[0] * aspect_ratio)
    else:
        new_width = width
        new_height = height

    cv2.resize(image, (new_width, new_height))

    # Set the font scale and thickness for the border
    font_scale = 1
    font_thickness = 2
    border_thickness = 5
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_color = (255, 255, 255)
    hilight_color = (0, 0, 0)

    # Get the size of the text
    text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)

    # Calculate the position for the border
    x1 = x - border_thickness
    y1 = y - border_thickness-text_size[1]
    x2 = x + text_size[0] + border_thickness
    y2 = y + text_size[1] + border_thickness-text_size[1]

    cv2.rectangle(image, (x1, y1), (x2, y2), hilight_color, -1)  # -1 fills the rectangle
    cv2.putText(image, text, (x, y), font, font_scale, text_color, font_thickness)

def getFrameRange(frameName):
    endFrame=0
    startFrame=0
    try:
        endFrame = frameRangeJson[frameName][1]
        startFrame = frameRangeJson[frameName][0]
    except FileNotFoundError as e:
        print("File not found:", e)
    except json.decoder.JSONDecodeError as e:
        print("Error decoding JSON:", e)
    except KeyError as e:
        print("Key not found:", e)
        
    return startFrame,endFrame

def add_text_to_image(image_path, text, position=(10, 50), font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=1, color=(255, 255, 255), thickness=2):
    # Read the image
    image = cv2.imread(image_path)

    # Add text to the image
    cv2.putText(image, text, position, font, font_scale, color, thickness)
    cv2.imwrite(image_path, image)
    print ("tadaa")
    return image
    


imageDir = r"M:\MECHA\02_ressource\@LOUIS\ressources\thumbnail\seq040"

with open(r"\\MINERVA\3d4_23_24\MECHA\02_ressource\@LOUIS\ressources\thumbnail\timeRanges.json", 'r') as file:
    frameRangeJson = json.load(file)

thumbnails = os.listdir(imageDir)
png_files = [file_path for file_path in thumbnails if file_path.lower().endswith(".png")]

for imageName in png_files:

    name, extension = os.path.splitext(imageName)
    print(name)

    startFrame,endFrame=getFrameRange(name)
    frame_range = f"{startFrame}/{endFrame}"
    print(f"frame range = {startFrame}/{endFrame}")

    image_path = os.path.join(imageDir,imageName)
    text = os.path.basename(image_path)
    position = (10, 30)
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 2
    border_thickness = 5
    color = (0, 0, 0)  # white color in BGR
    thickness = 2

    
    image = cv2.imread(image_path)
    resized_image = resize_image(image, width=1024, height=427)
    cv2.imwrite(image_path, resized_image)

    image = cv2.imread(image_path)
    high_lighted_text(image,text,position[0],position[1],font_scale, width=1024, height=427)
    cv2.imwrite(image_path, image)

    image = cv2.imread(image_path)
    high_lighted_text(image,frame_range,10,70,font_scale, width=1024, height=427)
    cv2.imwrite(image_path, image)
    


