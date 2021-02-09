import cv2
from os import path
from .bodyPartsDetection import recognition

def load_images_from_folder():
    folder = '/media/knowYourself/imageDB/'
    images = []
    iterator = 1
    while path.exists(folder + str(iterator) + '.jpg'):
        images.append(folder + str(iterator) + '.jpg')
        print(folder + str(iterator) + '.jpg')
        iterator += 1
    return images
