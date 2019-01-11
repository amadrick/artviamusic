from django.db import models

# Create your models here.
class Job(models.Model):
    # Image
    image = models.ImageField(upload_to='images/')
    #Title
    title = models.CharField(max_length=100, default='')
    # Summary
    summary = models.CharField(max_length=200)
    # Song
    song= models.CharField(max_length=200, default="Song: 'TITLE' - ARTIST (YEAR)")
    # Art
    art = models.CharField(max_length=200, default="Art: 'TITLE' - ARTIST (YEAR)")
    # Write up
    write_up = models.CharField(max_length=10000, default='')
    # Spotify
    spotify = models.CharField(max_length=200, default="Add 'embed' between '...com/' and '/track...'")
    #Text Field (test)
    text = models.TextField(default="test")

    # Google Maps #
    # map = models.CharField(max_length=5000, default="Just add URL")

    def __str__(self):
        return self.summary