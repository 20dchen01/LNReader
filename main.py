
from PIL import Image
from pytesseract import pytesseract

#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Define path to image
path_to_image = 'images/V3Chapter4.jpg'

#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

#Open image with PIL
img = Image.open(path_to_image)

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
