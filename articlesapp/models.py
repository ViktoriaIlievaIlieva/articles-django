from django.db import models


class Articles(models.Model):
    title = models.TextField()
    content = models.TextField()
    publish_date = models.DateField()

