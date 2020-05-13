from django.urls import path, include
from choosing.views import *

urlpatterns = [
    path('candidates/', Choosing.as_view()),
    path('get_status/', Status.as_view()),
    path('remember_id/', FakeVote.as_view()),
]