from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404
def home(request):
    oqituvchilar = Teacher.objects.all()
    videos = VideoUpload.objects.all()
    return render(request, 'home.html', {'oqituvchilar': oqituvchilar, 'videos': videos})

def certificate_detail(request, id):
    certificate = get_object_or_404(Certificate, id=id)
    return render(request, 'certificate_detail.html', {'certificate': certificate})




