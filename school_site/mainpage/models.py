from django.db import models
from PIL import Image


class Article(models.Model):
    class Meta:
        db_table = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ['-date_create']

    title = models.CharField(max_length=250, verbose_name='Заголовок')
    date_create = models.DateTimeField(u'Дата публикации', auto_now=True)
    content = models.TextField(max_length=10000)
    views = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True)

    def __unicode__(self):
        return self.title
    
