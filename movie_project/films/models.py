from django.db import models

# Create your models here.

class News_post(models.Model):
    title = models.CharField('Название фильма', max_length=50)
    short_description = models.CharField('Жанр', max_length=200)
    text = models.TextField('Описание фильма')
    responce1 = models.TextField('Популярный отзыв')
    responce2 = models.TextField('Отрицательный отзыв')
    raiting = models.CharField('Рейтинг', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
