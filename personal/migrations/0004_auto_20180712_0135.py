# Generated by Django 2.0.7 on 2018-07-11 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0003_auto_20180709_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='recycle',
            name='image',
            field=models.FileField(upload_to=''),
        ),
    ]
