from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from users import serializers
from users import models

class UsersViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )

    serializer_class = serializers.UsersSerializer
    queryset = models.User.objects.all()