from dataclasses import fields
from rest_framework import serializers
from apphos.models.Login import login

class loginserializer(serializers.ModelSerializer):
     
 class Meta:
        model=login
        fields=('self', 'username', 'password')

