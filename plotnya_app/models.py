from django.db import models

# Create your models here.
class Photos (models.Model):
    caption = models.CharField(max_length=140)
    photo = models.ImageField(upload_to='./media/galery')
