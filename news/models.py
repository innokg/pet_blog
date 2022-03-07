from django.db import models
from django.urls import reverse #строит ссылку в Python формате, то же что URLS (для шаблонов)


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    content = models.TextField(blank=True,  verbose_name='Контент') #можно не заполнять
    created_at = models.DateTimeField(auto_now_add=True,  verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True,  verbose_name='Обновлено')
    image = models.ImageField(upload_to='images/%Y/%m/%d/',  verbose_name='Картинка', blank=True) #позволяет сохранять в БД изображения, filefield позволяет любой тип данных сохранять
    is_published = models.BooleanField(default=True,  verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')# внешний ключ к категориям
    views = models.IntegerField(default=0, verbose_name='Просмотры')

    def get_absolute_url(self): #функция чтобы получить путь к одному объекту категории
        return reverse('view_news', kwargs={"pk": self.pk})

    # def my_func(self):        функция для того чтобы показать что мы можем вызывать методы в шаблонах
    #     return 'Hello from model'


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Название категории') # индексирование для более быстрого поиска в БД

    def get_absolute_url(self): #функция чтобы получить путь к одному объекту категории
        return reverse('category', kwargs={"category_id": self.pk})


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']