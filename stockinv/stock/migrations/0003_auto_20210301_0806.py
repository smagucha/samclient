# Generated by Django 3.1.6 on 2021-03-01 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20210301_0743'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Catgory',
        ),
        migrations.DeleteModel(
            name='Manufacturer',
        ),
        migrations.DeleteModel(
            name='stock',
        ),
    ]
