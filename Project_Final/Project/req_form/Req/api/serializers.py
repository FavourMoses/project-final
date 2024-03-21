from rest_framework import serializers
from Req.models import Requisition
from django.contrib.auth.models import User
from Req.forms import ApprovalForm


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requisition
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

class ApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requisition
        fields = ['approved']