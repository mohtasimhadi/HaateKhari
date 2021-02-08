from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
  
# Create your views here. 
def add_image_know_you(request):
    if request.method == 'POST':
        form = KnowYourSelfForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = KnowYourSelfForm
    return render(request, 'add_image_know_you.html', {'form' : form})

 
def success(request): 
    return HttpResponse('successfully uploaded')