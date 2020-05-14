from django.urls import path, include
from user.views import *

urlpatterns = [
    path('login/', Login.as_view()),
    path('filter/', Filter.as_view()),
]