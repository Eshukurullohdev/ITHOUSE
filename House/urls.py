from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path("teacher_detail", detail_view, name="detail_view")
]
