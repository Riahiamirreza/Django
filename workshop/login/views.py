from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login 
from login.serializers import UserloginSerializer 
from rest_framework import serializers                                                   

                            
def login2(request):                      
    try:                  
        data = request.POST
        print(data)
        serializer = UserloginSerializer(data=data)
        s = serializer.is_valid()
        if s :
            user =authenticate(
                username=request.POST['username'],
                password=request.POST['password']
            )
            print(user)
            if user:
                login(request,user)
                return JsonResponse(
                    {
                        'message': 'you are login'
                    },status=200
                )
            else:
                return JsonResponse(
                    {
                        'message' : 'username or password wrong!'
                    },status=401
                )
        else:
            return JsonResponse(
                {
                    'message' : 'wrong request'
                },status=400
            )
    except IntegrityError:
        return JsonResponse(
            {
                'message' : '0'
            },status=400
        )

# after learning git
