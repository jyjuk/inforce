from rest_framework import generics, permissions
from .serializers import EmployeeSerializer


class EmployeeCreateView(generics.CreateAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAdminUser,)