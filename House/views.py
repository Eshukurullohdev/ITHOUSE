from django.shortcuts import render
from .models import *
def home(request):
    oqituvchilar = Teacher.objects.all()
    videos = VideoUpload.objects.all()
    return render(request, 'home.html', {'oqituvchilar': oqituvchilar, 'videos': videos})




