from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('certificate/', find_certificate, name='find_certificate'),
]
