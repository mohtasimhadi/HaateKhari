import cv2
import os
from django.db import models
from PIL import Image
from .bodyPartsDetection import bodyPartDetection


# Create your models here.


class bodyPartsDetection(models.Model):
    actions = [ ('nose', 'nose'),
                ('frontalFace', 'frontalFace'),
                ('eye', 'eye'),
                ('mouth', 'mouth')
    ]
    image = models.ImageField(upload_to='media/knowYourself')
    action = models.CharField(max_length=11, choices=actions, default=None)

    def __str__(self):
        return str(self.action)

    def save(self, *args, **kwargs):
        temp_location = "media/knowYourself/temp.jpg"

        # open image
        pil_img = Image.open(self.image)
        pil_img.save(temp_location)
        # calling function
        img = bodyPartDetection(cv2.resize(cv2.imread(temp_location),
                                           None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA), 'nose')
        # removing temp file
        try:
            os.remove(temp_location)
        except:
            pass

        # save
        cv2.imwrite("media/knowYourself/result.jpg", img)