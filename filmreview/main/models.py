from django.db import models


class Film(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Название фильма'
        verbose_name_plural = 'Названия фильмов'