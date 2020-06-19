from django.db import models

class ContactMsg(models.Model):
    contact_name=models.CharField(max_length=30)
    contact_email=models.CharField(max_length=30)
    contact_msg=models.CharField(max_length=300)

