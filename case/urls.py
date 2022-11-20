from django.urls import path, include
# from rest_framework.routers import SimpleRouter 

from .views import CaseAPI
# router = SimpleRouter()
# router.register("", CaseAPI, 'case')
# urlpatterns = [
#     path("", include(router.urls))
# ]

urlpatterns = [
    path('get/case/',CaseAPI.as_view())
]

