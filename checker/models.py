from django.db import models


class Url(models.Model):
    url = models.URLField(max_length=255)

    def __str__(self):
        return self.url
