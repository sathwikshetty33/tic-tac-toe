from django.db import models

# Create your models here.
class Game(models.Model):
    room_code = models.CharField(max_length=10)
    creator = models.CharField(max_length=100)
    opponent = models.CharField(max_length=100,blank=True,null=True)
    over = models.BooleanField(default=False)
    def __str__(self):
        return self.room_code
    
