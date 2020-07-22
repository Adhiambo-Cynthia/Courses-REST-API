"""
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')"""
from django.urls import path, include
from . import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('courses', views.CourseView)

urlpatterns=[
    path('', include(router.urls))
]