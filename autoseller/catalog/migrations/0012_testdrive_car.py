# Generated by Django 4.2.5 on 2023-11-02 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_testdrive'),
    ]

    operations = [
        migrations.AddField(
            model_name='testdrive',
            name='car',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='test_drives', to='catalog.cars'),
            preserve_default=False,
        ),
    ]
