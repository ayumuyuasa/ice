# Generated by Django 2.1.5 on 2019-04-08 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.URLField(verbose_name='画像'),
        ),
    ]
