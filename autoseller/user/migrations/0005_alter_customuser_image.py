# Generated by Django 4.2.5 on 2023-10-24 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='user/img/profile.png', upload_to='user/static/user/img', verbose_name='Аватар'),
        ),
    ]
