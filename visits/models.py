from django.db import models


class Worker(models.Model):
    """Модель работника"""
    name = models.CharField(max_length=255, verbose_name='Имя')
    phone_number = models.CharField(max_length=255, verbose_name='Номер телефона', unique=True)

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return self.name


class Store(models.Model):
    """Модель торговая точка"""
    name = models.CharField(max_length=255, verbose_name='Название')
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='stores')

    class Meta:
        verbose_name = 'Торговая точка'
        verbose_name_plural = 'Торговые точки'

    def __str__(self):
        return self.name


class Visit(models.Model):
    """Модель посещение"""
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True, verbose_name='Торговая точка', related_name='visit')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')

    class Meta:
        verbose_name = 'Посещение'
        verbose_name_plural = 'Посещения'

    def __str__(self):
        return f"Visit to {self.store} at {self.date_created}"
