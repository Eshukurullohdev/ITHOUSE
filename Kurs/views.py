from django.shortcuts import render

def kursPython(request):
    return render(request, 'kursPython.html')


def kursEnglish(request):
    return render(request, 'kursEnglish.html')