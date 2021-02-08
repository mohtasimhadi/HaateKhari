import cv2
import os
import random
from os import path
from django.db import models
from PIL import Image
from .bodyPartsDetection import bodyPartDetection


# Create your models here.

class bodyPartDetection(models.Model):
    imageName = 0
    while path.exists('knowYourself/imageDB'+str(imageName)+'.jpg'):
        imageName += 1
    image = models.ImageField(upload_to='knowYourself/imageDB/'+str(imageName)+'.jpg')


# class bodyPartsDetection(models.Model):

#     image = models.ImageField(upload_to='media/knowYourself')

#     def __str__(self):
#         return str(self.action)

#     def save(self, *args, **kwargs):
#         temp_location = "media/knowYourself/temp/temp.jpg"

#         # select action

#         action = random.choice(['frontalFace', 'eye', 'mouth', 'nose'])

#         # open image
#         pil_img = Image.open(self.image)
#         pil_img.save(temp_location)
#         # calling function
#         img = bodyPartDetection(cv2.resize(cv2.imread(temp_location),
#                                            None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA), action)
#         # removing temp file
#         try:
#             os.remove(temp_location)
#         except:
#             pass

#         # save
#         cv2.imwrite("media/knowYourself/"+action+".jpg", img)