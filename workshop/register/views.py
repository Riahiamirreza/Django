from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework import serializers
from register.serializers import UserSerializer


def register(request):
    print(request.POST)
    try:
        data = request.POST
        serializer = UserSerializer(data=data)
        u = serializer
        s = serializer.is_valid()
        if s :
            u.save()
            return JsonResponse({
                'message' : 'saved'
            }, status=201)
        else:
            return JsonResponse(
                {
                    'message' : 'request  wrong'
                },status=400
            )
    except IntegrityError:
        return JsonResponse({
            'message' : 'username was token !'
        }, status=400)