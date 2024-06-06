from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Base(models.Model):
    created_by = models. ForeignKey (User, on_delete=models.PROTECT, related_name="+", null=True)
    created_at = models.DateTimeField(null=True)
    updated_by = models. ForeignKey (User, on_delete=models.PROTECT, related_name="+", null= True)
    updated_at = models.DateTimeField(null=True)
    is_delete = models. BooleanField(default=False)
    
    class Meta:
        abstract = True

class Student(Base):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=10)
    roll_no = models.IntegerField()

    class Meta:
        db_table = 'student'