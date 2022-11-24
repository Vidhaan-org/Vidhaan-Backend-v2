from django.urls import path, include

from .views import *

urlpatterns = [
    path('/', Profile.as_view())
]

