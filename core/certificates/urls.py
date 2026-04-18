from django.urls import path
from .views import generate_certificate

urlpatterns = [
    path('generate/<int:course_id>/', generate_certificate, name='generate_certificate'),
]