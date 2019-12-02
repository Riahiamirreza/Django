from django.shortcuts import render
from django.contrib.auth.models import AnonymousUser
from django.http import JsonResponse
from register.serializers import UserSerializer
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt, CsrfViewMiddleware
from django.views.decorators.csrf import get_token
from chat.serializers import MessageSerializer


class ChatView(APIView):
    @csrf_exempt
    def put(request):
        if request.user.is_authenticated:
            print(request.POST)
            s = UserSerializer(instance=request.user, data=request.POST)
            print(s)
            if s.is_valid():
                s.save()
                return Response(
                    {
                        'message': 'profile edited!'
                    }, status=201
                )
        else:
            return Response(
                {
                    'message' : 'you are not login!'
                },status=401
            )


def profile(request):
    if request.user.is_authenticated:
        # data = {
        #     'username': request.user.username,
        #     'email' : request.user.email
        # }
        serializer = UserSerializer(request.user)
        a = serializer.data
        return JsonResponse(
            {
                'profile' : a
            },status=200
        )
    else:
        return JsonResponse(
            {
                'message' : 'you are not login'
            },status=401
        )
    


def message(request):
    if request.user.is_authenticated:
        data = request.POST
        MessageSerializer.sender = request.user.id
        MessageSerializer.receiver = request.POST['receiver']
        MessageSerializer.text = request.POST['text']
        serializer = MessageSerializer(data=data)
        m = serializer
        print(m)
        s = m.is_valid()
        if s:
            m.save()
            return JsonResponse(
                {
                    'message' : 'message saved'
                }, status=201
            )
        else:
            return JsonResponse(
                {
                    'message' : 'invalid message'
                }, status=400
            )
    else:
        return JsonResponse(
            {
                'message' : 'You are not login'
            }, status=401
        )

# def conversation(request):
#     if request.user.is_authenticated:




# def edit(request):
#     if request.user.is_authenticated:
#         data = request.POST
#         s = UserSerializer(data=data)
#         print(f'======>{s}')
#         u = s.is_valid()
#         if u:
#             s.update(request.user.username,request.POST['username'])
#             return JsonResponse(
#                 {
#                     'message' : 'profile edited!'
#                 },status=201
#             )
#         else:
#             return JsonResponse(
#                 {
#                     'message' : 'wrong request'
#                 }
#             )
#     else:
#         return JsonResponse(
#             {
#                 'message' : 'you are not login!'
#             },status=401
#         )







# def creat_group(request):
#     if request.user.is_authenticated: