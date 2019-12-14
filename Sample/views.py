from django.shortcuts import render
from rest_framework import viewsets
from .models import Assignment
from .serializers import AssignmentSerializer

class AssignmentView(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer