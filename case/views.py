from django.contrib.auth import get_user_model 
from django.db import models
from django.db.models import Q
# from rest_framework.viewsets import GenericViewSet

from rest_framework.generics import GenericAPIView 
from rest_framework.response import Response 
from rest_framework.decorators import action 

from .models import *
from .serializers import * 
Users = get_user_model()


# class CaseAPI(GenericViewSet):
#     # permission_classes = [HasValidToken]
#     user_instance = None 

#     @action(
#         detail = False, 
#         methods = ["get"], 
#         url_path = "get-cases"
#     )
#     def get_cases(self, request): 
#         cases = []
#         try: 
#             user_instance = Users.objects.get(mobile = self.user_instance) 
#             cases = Case.objects.filter(
#                     Q(petitioner__contains = user_instance) | Q(respondent__contains = user_instance) | Q(petitioner_advocate__contains = user_instance) | Q(respondent_advocate__contains = user_instance))
#         except Users.DoesNotExist: cases = Case.objects.all()
        
#         case_data = CaseSerializer(cases, many = True).data 
#         # if not case_data: 
#         #     return Response(cases) 
#         print(case_data)
#         return Response({})


class CaseAPI(GenericAPIView):
    # permission_classes = [HasValidToken]
    # user_instance = None 

    def get(self, request): 
        cases = Case.objects.all()
        try: 
            user_instance = Users.objects.get(mobile = request.user_instance) 
            cases = Case.objects.filter(
                    Q(petitioner__contains = user_instance) | Q(respondent__contains = user_instance) | Q(petitioner_advocate__contains = user_instance) | Q(respondent_advocate__contains = user_instance))
        except Users.DoesNotExist: cases = Case.objects.all()
        
        case_data = CaseSerializer(cases, many = True).data 

        print(case_data)
        if case_data:
            return Response(case_data)
        else: 
            print("noooooooo")
            return Response({})

