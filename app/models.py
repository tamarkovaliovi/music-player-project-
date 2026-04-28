from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=200) 
    artist = models.CharField(max_length=200)
    image = models.ImageField(upload_to='music_images/')
    audio_file = models.FileField(upload_to='musics/')
    
    lyrics_data = models.TextField(blank=True, null=True, help_text='Örn: [{"time": "0:05", "text": "Merhaba dünya"}]')

    def __str__(self):
        return self.title