from django.db import models

class AnnotatedImage(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='images/')
    class_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='pending')  # 'pending' or 'annotated'
