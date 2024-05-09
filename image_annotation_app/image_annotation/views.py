import json
from django.http import JsonResponse
from .models import AnnotatedImage
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile
import base64

@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            format, imgstr = data['image'].split(';base64,')
            ext = format.split('/')[-1]
            img = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

            image_instance = AnnotatedImage(
                image=img,
                class_name=data['class_name'],
                status='pending'
            )
            image_instance.save()

            return JsonResponse({'id': image_instance.id, 'status': 'Image saved'}, status=201)
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        except KeyError as e:
            return JsonResponse({'error': str(e) + ' key is missing'}, status=400)
        except Exception as e:
            return JsonResponse({'error': 'Error processing your request', 'details': str(e)}, status=500)


from .models import AnnotatedImage

def search_images(request):
    class_name = request.GET.get('class_name', '')
    images = AnnotatedImage.objects.filter(class_name__icontains=class_name).values('id', 'image', 'class_name')
    return JsonResponse({'results': list(images)})


from django.views.generic import UpdateView
from .models import AnnotatedImage

class UpdateAnnotatedImageView(UpdateView):
    model = AnnotatedImage
    fields = ['class_name']

    def form_valid(self, form):
        form.save()
        return JsonResponse({'message': 'Class name updated successfully.'})
