from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField('タイトル', max_length=100)
    text = models.TextField('本文')
    created_at = models.DateTimeField('作成日', default=timezone.now)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
