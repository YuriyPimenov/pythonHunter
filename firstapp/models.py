from django.db import models

# Create your models here.
class PizzaShop(models.Model):
    name = models.CharField(max_length=30, verbose_name='Пиццерия')
    description = models.TextField(verbose_name='Описание')
    rating = models.FloatField(default=0, verbose_name='Рейтинг')
    url = models.URLField(verbose_name='Интернет-адрес пиццерии')

    class Meta:
        verbose_name='Пиццерия'
        verbose_name_plural='Пиццерии'

    def __str__(self):
        return self.name

class Pizza(models.Model):
    PizzaShop = models.ForeignKey(PizzaShop, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='Название пиццы')
    short_description = models.CharField(max_length=30, verbose_name='Краткое описание')
    price = models.IntegerField(default=0, verbose_name='Цена')
    #blank=true - Позволяет добавлять пиццу без фото
    photo = models.ImageField('Фото', upload_to = 'firstapp/photos', default='',blank=True)
    
    class Meta:
            verbose_name='Пицца'
            verbose_name_plural='Пиццы'
            ordering=['name']

    def __str__(self):
        return self.name

class Order(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, verbose_name='Пицца')
    name = models.CharField(max_length=30, verbose_name='Имя')
    phone = models.CharField(max_length=30, verbose_name='Телефон')
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")