from django.db import models

# Create your models here.



# Create your models here.
from users.models import User
from courses.models import Courses

class Certificates(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     course = models.ForeignKey(Courses, on_delete=models.CASCADE)
     issued_at = models.DateTimeField(auto_now_add=True)
     unique_id=models.CharField(max_length=20) 

