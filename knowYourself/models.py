import cv2
import os
from django.db import models
from PIL import Image
from .bodyPartsDetection import bodyPartDetection


# Create your models here.


class bodyPartsDetection(models.Model):
    image = models.ImageField(upload_to='result_dump')

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        temp_location = "knowYourself/result_dump/temp.jpg"

        # open image
        pil_img = Image.open(self.image)
        pil_img.save(temp_location)
        # calling function
        # actions = mouth, eye, frontalFace, nose
        action = 'nose'
        img = bodyPartDetection(cv2.resize(cv2.imread(temp_location),
                                           None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA), action)
        # removing temp file
        try:
            os.remove(temp_location)
        except:
            pass

        # save
        cv2.imwrite("knowYourself/result_dump/result.jpg", img)