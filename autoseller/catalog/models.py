from django.contrib.auth.models import User
from django.db import models


class Cars(models.Model):
    brand = models.CharField('Марка', max_length=25)
    model = models.CharField('Модель', max_length=25)
    price = models.FloatField('Стоимость')
    date = models.DateField('Дата выпуска')
    img = models.ImageField(upload_to='static/img', verbose_name='Фотография')
    fuel_type = [('Дизель', 'Дизель'), ('Бензин', 'Бензин')]
    fuel = models.CharField('Тип топлива', choices=fuel_type, default='Бензин', max_length=20)
    mileage = models.IntegerField('Пробег')
    engine = models.FloatField('Объем двигателя')
    body = [
        ('Универсал', 'Универсал'),
        ('Седан', 'Седан'),
        ('Хэтчбек', 'Хэтчбек'),
        ('Кабриолет', 'Кабриолет'),
        ('Внедорожник', 'Внедорожник'),
        ('Кроссовер', 'Кроссовер'),
        ('Купе', 'Купе'),
        ('Лифтбек', 'Лифтбек'),
        ('Пикап', 'Пикап'),
        ('Минивен', 'Минивен'),
        ('Лифтбек', 'Лифтбек')
    ]
    body_type = models.CharField('Тип кузова', choices=body, default='Седан', max_length=20)
    gearbox = [('Механическая', 'Механическая'),
               ('Автомат', 'Автомат')]
    gear = models.CharField('Коробка передач', choices=gearbox, default='Автомат', max_length=20)
    drive = [('Передний', 'Передний'), ('Задний', 'Задний'), ('Полный', 'Полный')]
    drive_type = models.CharField('Привод', choices=drive, default='Задний', max_length=20)
    color = models.CharField('Цвет', max_length=15)

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def get_absolute_url(self):
        return f'/catalog/{self.id}'


class TestDrive(models.Model):
    test_date = models.DateTimeField('Дата тест-драйва')
    duration = models.IntegerField('Длительность тест-драйва')
    car = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name='test_drives')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')

    class Meta:
        verbose_name = 'ТестДрайв'
        verbose_name_plural = 'ТестДрайвы'

    def __str__(self):
        return f'{self.car} {self.user}'
