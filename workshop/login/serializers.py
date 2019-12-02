from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class UserloginSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=50)
    password=serializers.CharField(max_length=50)





        

