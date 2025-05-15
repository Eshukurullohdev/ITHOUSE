from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
     path('certificate/<int:id>/', certificate_detail, name='certificate_detail'),
]
