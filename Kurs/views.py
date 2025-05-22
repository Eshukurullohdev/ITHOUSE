from django.shortcuts import render

def kursPython(request):
    return render(request, 'kursPython.html')


def kursEnglish(request):
    return render(request, 'kursEnglish.html')


def kursReact(request):
    return render(request, 'kursReact.html')

def kursRus(request):
    return render(request, 'kursRus.html')