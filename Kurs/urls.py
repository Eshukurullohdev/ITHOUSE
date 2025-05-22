from django.urls import path
from .views import *

urlpatterns = [
    path('kursPython/', kursPython, name='kursPython'),
    path("kursEnglish/", kursEnglish, name="kursEnglish"),
    path("kursReact/", kursReact, name="kursReact"),
]
