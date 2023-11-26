# Generated by Django 4.2.5 on 2023-11-01 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_alter_cars_fuel'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestDrive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_date', models.DateTimeField(verbose_name='Дата тест-драйва')),
                ('duration', models.IntegerField(verbose_name='Длительность тест-драйва')),
            ],
            options={
                'verbose_name': 'ТестДрайв',
                'verbose_name_plural': 'ТестДрайвы',
            },
        ),
    ]
