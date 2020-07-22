from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields= '__all__'

#ModelSerializer class is simply a shortcut for creating serializer classes with 
#An automatically determined set of fields.
# Simple default implementations for the create() and update() methods