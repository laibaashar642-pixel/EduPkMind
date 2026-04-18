from django.contrib import admin

# Register your models here.
from courses.models import Courses,Lesson
admin.site.register(Courses)
admin.site.register(Lesson)

