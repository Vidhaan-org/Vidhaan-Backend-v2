from django.contrib.auth import get_user_model 
from django.db import models
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import GenericAPIView 
from rest_framework.response import Response 
from django_filters.rest_framework import *

from .models import *
from .serializers import *
Users = get_user_model()


class CaseAPI(GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, ]

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['cnr_number'] 
    ordering_fields = ['cnr_number', 'filing_number','next_hearing_date','registration_number', 'case_status']

    def get(self, request): 
        query=self.request.query_params.get('query')
        
        try: 
            user_instance = request.user
            cases = Case.objects.filter(Q(petitioner = user_instance) | Q(respondent = user_instance) | Q(petitioner_advocate = user_instance) | Q(respondent_advocate = user_instance))
             
        except Users.DoesNotExist: 
            cases = Case.objects.all()
        
        if query:  
            cases = cases.filter(Q(cnr_number__icontains = query) | Q(fir_number__icontains = query) | Q(cnr_number__iexact = query) | Q(petitioner__first_name__icontains = query) | Q(respondent__first_name__icontains = query) | Q(petitioner_advocate__first_name__icontains = query) | Q(respondent_advocate__first_name__icontains = query) | Q(under_act__icontains = query) | Q(case_type__icontains = query)) 
        else:  pass 

        if cases: 
            case_data = CaseSerializer(cases, many = True).data 
        else: 
            return Response({
                "message": "no case for this search"
            })

        if case_data:
            return Response({
                "data": case_data
            })
        else: 
            return Response({
                "message": "you didn't have any case registered on your number"
            }) 

    def post(self,request):
        serializer=CaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({
                "data": serializer.data
            })
        else: 
            return Response({
                "data": serializer.errors
            })
    