from rest_framework import serializers
# from django.contrib.auth.models import Group
from chat.models import Group2, Message


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group2
        feilds = (
            'name' , 'members' , 'is_admin'
        )
    
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            'sender', 'receiver', 'text', 'date'
        )

# class MessageSerializer(serializers,Serializer):