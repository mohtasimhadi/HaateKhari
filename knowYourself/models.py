import cv2
import os
import random
from os import path
from django.db import models
from PIL import Image
from .bodyPartsDetection import bodyPartDetection


# Create your models here.

class bodyPartDetection(models.Model):
    image = models.ImageField(upload_to='knowYourself/imageDB')

class test(models.Model):
    path = models.CharField(max_length=50)