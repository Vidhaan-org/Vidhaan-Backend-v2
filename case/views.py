from django.contrib.auth import get_user_model 
from django.db import models
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import GenericAPIView 
from rest_framework.response import Response 

from .models import *
from .serializers import CaseSerializer
Users = get_user_model()


class CaseAPI(GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, ]

    def get(self, request): 
        
        cases = Case.objects.all()
        case_data = CaseSerializer(cases,many = True).data

        if case_data:
            return Response(case_data)
        else: 
            return Response({}) 

