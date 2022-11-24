from django.urls import path, include

from .views import CaseAPI

urlpatterns = [
    path('/',CaseAPI.as_view())
]

