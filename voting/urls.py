from django.urls import path, include
from voting.views import *

urlpatterns = [
    path('', index, name='index'),
]