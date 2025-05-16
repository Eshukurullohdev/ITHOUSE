from django.urls import path
from .views import *

urlpatterns = [
    path('kursPython/', kursPython, name='kursPython'),
]
