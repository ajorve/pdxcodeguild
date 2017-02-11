"""
Rotate Image CLI Tool Program
"""


from PIL import Image
import os, sys


MEDIA_PREFIX = '/Users/Anders/Pictures/Anders_Old_Pics/My_Pictures/'


def image_collection():
    image_options = [i for i in os.listdir(MEDIA_PREFIX) if 'jpg' or 'jpeg' in i]
    images = dict(enumerate(image_options))

    print('To rotate an image, please select from one of the images below:', end='\n')
    for opt, name in images.items():
        print(opt, '>>', name)
    print('or', 'q) Quit', sep='\n', end='\n')

    user_selection = int(input('Please make your selection. >> '))

    if user_selection == "q":
        sys.exit()

    image_selection = images[user_selection]

    filename, file_type = image_selection.split('.')

    return filename, file_type, image_selection


def image_conversion(image_selection, filename):
    original_image = Image.open(MEDIA_PREFIX+image_selection)
    rotated_image = original_image.rotate(45)
    rotated_name = MEDIA_PREFIX + filename + '_rotated.jpg'
    rotated_image.save(rotated_name, 'JPEG')

    print(f"This {filename} has been rotated and named {rotated_name}")
    print(original_image.format, original_image.size, original_image.mode)


def load():
    filename, file_type, fullname = image_collection()
    image_conversion(fullname, filename)