from django.contrib import admin
from django.urls import path
from api.views import upload_image, process_image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', upload_image, name='upload_image'),  # Root URL
    path('process-image/', process_image, name='process_image'),  # API endpoint
]