import cv2
import os
import random
from os import path
from django.db import models
from PIL import Image
from .bodyPartsDetection import bodyPartDetection

# Create your models here.

class BodyPartDetection(models.Model):
    tempImage = models.ImageField(upload_to='media/knowYourself/temp/uploads')
    dir = 'media/knowYourself/imageDB/'
    def __str__(self):
        return(self.id)
    
    def save(self, *args, **kwargs):
        image = Image.open(self.tempImage)
        num_files = len(os.listdir('media/knowYourself/imageDB/'))
        image.save('media/knowYourself/imageDB/'+str(num_files)+'.jpg')


class test(models.Model):
    path = models.CharField(max_length=50)
