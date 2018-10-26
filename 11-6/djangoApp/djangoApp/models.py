from django.db import models



class Page(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    href = models.URLField(max_length=2084)
