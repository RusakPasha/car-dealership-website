# Generated by Django 4.2.5 on 2023-10-02 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='img',
            field=models.ImageField(upload_to='', verbose_name='Фотография'),
        ),
    ]
