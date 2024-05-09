from django.urls import path
from .views import upload_image
from .views import search_images
from .views import UpdateAnnotatedImageView

urlpatterns = [
    path('images/', upload_image, name='upload_image'),
    path('images/search/', search_images, name='search_images'),
    path('api/images/<int:pk>/', UpdateAnnotatedImageView.as_view(), name='update-annotated-image'),
]




