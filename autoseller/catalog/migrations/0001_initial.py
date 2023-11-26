# Generated by Django 4.2.5 on 2023-10-02 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=25, verbose_name='Марка')),
                ('model', models.CharField(max_length=25, verbose_name='Модель')),
                ('price', models.FloatField(verbose_name='Стоимость')),
                ('date', models.DateField(verbose_name='Дата выпуска')),
                ('img', models.ImageField(height_field=200, upload_to='', verbose_name='Фотография', width_field=200)),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
    ]