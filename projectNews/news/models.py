from django.db import models
from django.urls import reverse


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT,verbose_name='Категория',null=True)

    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk}) ## тут мы создали метод объекта нашей модели и вернули метод reverse c двумя аргументами, в первом аргументе мы передаем имя ссылки и вторым аргументом kwargs мы создаем словарь берем category_id и присваеваем pk нашего обьекта модели.

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-title']