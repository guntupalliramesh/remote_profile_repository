from django.db import models

class ProfileReg(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_no = models.IntegerField()
    email = models.EmailField(max_length=100)
    subject = models.TextField(max_length=100)
    message = models.TextField(max_length=1000)