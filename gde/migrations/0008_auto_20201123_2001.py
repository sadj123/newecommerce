# Generated by Django 3.1.2 on 2020-11-24 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gde', '0007_videogame_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videogame',
            name='photo',
            field=models.ImageField(blank=True, upload_to='videogame/%Y/%m/%d/'),
        ),
    ]