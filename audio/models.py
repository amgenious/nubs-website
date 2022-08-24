from django.db import models
from datetime import datetime

import audio

# Create your models here.
class Audio(models.Model):
    cat = [("1", "Sunday Sermons"), ("2", "Bible Studies"), ("3", "Thursday Prayers")]
    title=models.CharField(max_length=100)
    category=models.CharField(choices=cat, max_length=100, blank=True)
    created_at=models.DateTimeField(default=datetime.now, blank=True)
    audio=models.FileField(upload_to="audio/")

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        # return self.name
        return super().__str__()
    

class President(models.Model):
    row = models.CharField(max_length=100)
    name = models.CharField(max_length=1000)
    year_of_office = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return super().__str__()
