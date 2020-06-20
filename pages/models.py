from django.db import models

class ContactMsg(models.Model):
    contact_name=models.CharField(max_length=30)
    contact_email=models.CharField(max_length=30)
    contact_msg=models.CharField(max_length=300)

class Topic(models.Model):
    topic_name=models.CharField(max_length=30)
    topic_TLDR=models.CharField(max_length=300)
    topic_body=models.CharField(max_length=3000)
    topic_last_modified=models.DateTimeField()
