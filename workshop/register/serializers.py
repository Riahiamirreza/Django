from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username','email','password'
        )
  
    def validate_password(self,password):
        password = make_password(password)
        print(password)
        return password
    
    # def update(self,isinstance, validated_data):
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.email = validated_data.get('email', instance.email)
    #     return instance










# def update(self, instance, validated_data):
#         instance.email = validated_data.get('email', instance.email)
#         instance.content = validated_data.get('content', instance.content)
#         instance.created = validated_data.get('created', instance.created)
#         return instance