from django.db import models

from django.urls import reverse

class Song(models.Model):
    song = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('song_edit', kwargs={'pk': self.pk})

