from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'language', 'price')
    list_display_links=('id', 'name')
    list_per_page=10

admin.site.register(Course, CourseAdmin)    
