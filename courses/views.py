from .models import Course
from .serializers import CourseSerializer
from rest_framework import viewsets
from django.shortcuts import render

class CourseView(viewsets.ModelViewSet):
    queryset= Course.objects.all()
    serializer_class= CourseSerializer



