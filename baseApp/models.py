from django.db import models
# Create your models here.


class Upload_mutiple_files_model(models.Model):
    file = models.FileField(upload_to="media/")
    # file = Size_Filter_FileField(upload_to='media/', content_types=['application/pdf',  'application/csv', 'application/doc', 'application/ppt', 'application/txt', 'image/jpeg', 'image/png', 'image/webp', 'image/gif', 'image/jpg', 'video/x-msvideo', 'video/mp4', 'audio/mpeg'], max_upload_size=100000)




