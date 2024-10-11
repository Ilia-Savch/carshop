from django.contrib.auth import get_user_model

from django.db import models


class Car(models.Model):
    photo = models.ImageField(
        upload_to='photos/%Y/%m/%d/',
        default=None,
        blank=True,
        null=True,
        verbose_name='Фото')
    name = models.CharField(max_length=100, verbose_name='Название модели')
    date = models.IntegerField(verbose_name='Год выпуска')
    price = models.IntegerField(verbose_name='Цена')
    about = models.TextField(
        default=None, blank=True,
        null=True, verbose_name='Описание')
    run = models.CharField(
        max_length=100, default=None,
        blank=True, null=True, verbose_name='Пробег')
    generation = models.CharField(
        max_length=100, default=None, blank=True, null=True, verbose_name='Поколение')

    def __str__(self):
        return self.name


class Basket(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(Car, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)


class PayModel(models.Model):
    first_name = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='Имя')
    second_name = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='Фамилия')
    adres = models.CharField(max_length=300, blank=True,
                             null=True, verbose_name='Адрес')
    email = models.CharField(max_length=300, blank=True,
                             null=True, verbose_name='Email')
    phone = models.IntegerField(
        blank=True, null=True, verbose_name='Номер телефона')

    product_id = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
