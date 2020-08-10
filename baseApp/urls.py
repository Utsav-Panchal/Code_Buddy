from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index, upload_image_view


urlpatterns = [
    path('', index, name="copypaste_index"),
    path('img/', upload_image_view, name="upload_image"),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = 'baseApp.views.handler404'
handler500 = 'baseApp.views.handler500'