from django.shortcuts import render
from .models import *

def home(request):
    oqituvchilar = Teacher.objects.all()
    videos = VideoUpload.objects.all()
    return render(request, 'home.html', {'oqituvchilar': oqituvchilar, 'videos': videos})

def find_certificate(request):
    certificate = None
    error = None

    if request.method == 'POST':
        id = request.POST.get('id')
        if id and id.isdigit():
            try:
                certificate = Certificate.objects.get(id=id)
            except Certificate.DoesNotExist:
                error = f"ID {id} uchun sertifikat topilmadi."
        else:
            error = "Iltimos, to'g'ri ID kiriting."

    return render(request, 'certificate.html', {'certificate': certificate, 'error': error})




