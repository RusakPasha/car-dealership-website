# Generated by Django 4.2.5 on 2023-10-24 23:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_customuser_name_customuser_second_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'Информация о пользователе', 'verbose_name_plural': 'Информация о пользователях'},
        ),
    ]
