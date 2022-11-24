from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django_filters.rest_framework import *
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model 
from .serializers import *
from .models import *

Users = get_user_model()

class Profile(APIView):
    def get(self, request):
        users=Users.objects.all()
        user_serializer = UserDetailsSerializer(users, many = True).data

        if user_serializer: 
            return Response({
                "data": user_serializer
            })
        else: 
            return Response({
                "message": "no users exist!"
            })

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            user_det = UserDetails()
            user_det.user = Users.objects.get(mobile = request.data['mobile'])
            user_det.save()

            return Response({
                "data": serializer.data
            })
        else:
            return Response({
                "data": serializer.errors
            })


    def patch(self, request, *args, **kwargs):
        if request.data:
            user = CustomUser.objects.get(mobile = request.data['mobile'])
            user_det = UserDetails.objects.get(user = user)

            data = request.data
            
            user_det.gender = data["gender"]
            user_det.user_type = data["user_type"]
            user_det.pin = data["pin"]
            user_det.address = data["address"]
            user_det.city = data["city"]
            user_det.district = data["district"]
            user_det.state = data["state"]
            user_det.country = data["country"]
            user_det.save()

        return Response({
            "data": UserDetailsSerializer(user).data
        })
        