from rest_framework import serializers
from .models import AnnotatedImage

class AnnotatedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnotatedImage
        fields = ['id', 'image', 'class_name', 'status']
