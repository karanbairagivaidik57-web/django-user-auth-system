from django.db import models

# Create your models here.
class detail(models.Model):
    username=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    password=models.CharField(max_length=40)
    class Meta:
        db_table='detail'
