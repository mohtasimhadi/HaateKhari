import os
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .bodyPartsDetection import recognition


# Create your views here.

def test(request):
    if request.method == 'POST':
        try:
            form = request.POST['path']
            return HttpResponse('lel')
        except:
            return render(request, 'test.html')
    return render(request, 'test.html')


def know_you(request):
    return render(request, 'know_you.html')


def add_image_know_you(request):
    if request.method == 'POST':
        form = KnowYourSelfForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Your photo updated successfully.")
            return redirect('add_image_know_you')
    else:
        form = KnowYourSelfForm()
    return render(request, 'add_image_know_you.html', {'form': form})


def know_you_learn(request):
    imagePath = 'media/knowYourself/imageDB/2.jpg'
    recognition(imagePath)
    return render(request, 'know_you_learn.html')


def know_you_identity(request):
    return render(request, 'know_you_identity.html')

def know_you_quiz(request):
    imagePath = 'media/knowYourself/imageDB/2.jpg'
    recognition(imagePath)
    return render(request, 'know_you_quiz.html')