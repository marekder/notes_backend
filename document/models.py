from django.db import models


class Document(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=100)
    note = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
