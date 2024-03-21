from Req.models import Requisition
from Req.api.serializers import RequestSerializer
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .serializers import UserSerializer, RequestSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,)
from rest_framework.authtoken.views import obtain_auth_token

class RequestListView(generics.RetrieveAPIView):
    queryset = Requisition.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [permissions.AllowAny]


class UserListView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class ApproveListView(generics.RetrieveAPIView):
    queryset = Requisition.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [permissions.AllowAny]