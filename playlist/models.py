from django.db import models

class Video(models.Model):
    title = models.CharField(max_length = 200)
    embed_code = models.TextField(default="")
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
