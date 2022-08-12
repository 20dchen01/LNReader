from PIL import Image
from pytesseract import pytesseract
import os

#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Define path to images folder
path_to_images = r'images/'

#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

#Get the file names in the directory
for root, dirs, file_names in os.walk(path_to_images):
    #Iterate over each file name in the folder
    for file_name in file_names:
        #Open image with PIL
        img = Image.open(path_to_images + file_name)

        #Extract text from image
        text = pytesseract.image_to_string(img)

        print(text)


# import subprocess
#
# # getting meta data of the wifi network
# meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
#
# # decoding meta data from byte to string
# data = meta_data.decode('utf-8', errors="backslashreplace")
#
# # splitting data by line by line
# # string to list
# data = data.split('\n')
#
# # creating a list of wifi names
# names = []
#
# # traverse the list
# for i in data:
#
#     # find "All User Profile" in each item
#     # as this item will have the wifi name
#     if "All User Profile" in i:
#         # if found split the item
#         # in order to get only the name
#         i = i.split(":")
#
#         # item at index 1 will be the wifi name
#         i = i[1]
#
#         # formatting the name
#         # first and last chracter is use less
#         i = i[1:-1]
#
#         # appending the wifi name in the list
#         names.append(i)
#
# # printing the wifi names
# print("All wifi that system has connected to are ")
# print("-----------------------------------------")
# for name in names:
#     print(name)
