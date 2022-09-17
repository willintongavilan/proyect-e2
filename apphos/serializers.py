from dataclasses import fields
from rest_framework import serializers
from .models import Paciente

class pacenteserializer(serializers.ModelSerializer):
     account = AccountSerializer()
    class Meta:
        model=Paciente
        fields='__all__'

    def create(self, validated_data):
        accountData = validated_data.pop('account')
        userInstance = User.objects.create(**validated_data)
        Account.objects.create(user=userInstance, **accountData)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        account = Account.objects.get(user=obj.id) 
        return {
            
            }
        }
