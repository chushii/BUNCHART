from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class articles(models.Model):
    title = models.CharField('Заголовок', max_length = 50)
    description = models.CharField('Описание', max_length = 200)
    text = models.TextField('Текст')
    data = models.DateTimeField('Дата публикации', default = datetime.now())
    author = models.ForeignKey(User, null = True, blank = True,
    on_delete = models.SET_NULL, verbose_name = 'Автор')
    
    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ["-data"]
        verbose_name_plural = 'новости'
        verbose_name = 'новость'

class pictures(models.Model):
    title = models.CharField('Заголовок', max_length = 50)
    image = models.FileField(default = 'temp.jpg', verbose_name = 'Путь к картинке')
    data = models.DateTimeField('Дата публикации', default = datetime.now())
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Автор')
    
    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ["-data"]
        verbose_name_plural = 'рисунки'
        verbose_name = 'рисунок'
    
class comments(models.Model):
    text = models.TextField('Текст комментария')
    data = models.DateTimeField('Дата комментария', default = datetime.now())
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Автор')
    post = models.ForeignKey(pictures, on_delete = models.CASCADE, verbose_name = 'Запись')
    
    def __str__(self):
        return '%s // %s (%d)' % (self.post, self.author, self.id)
        
    class Meta:
        ordering = ["-data"]
        verbose_name_plural = 'комментарии'
        verbose_name = 'комментарий'