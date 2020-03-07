from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from ai.models import project as ai_project

# Create your models here.
class aipost(models.Model):
    post_title = models.CharField(max_length=64,unique=True)
    post_image_address = models.ImageField(default='default.jpg',upload_to='post_images/ai')
    post_url = models.OneToOneField(ai_project,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.post_title}'