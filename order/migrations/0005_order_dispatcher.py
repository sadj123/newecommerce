# Generated by Django 3.1.2 on 2020-11-29 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gde', '0009_auto_20201128_1102'),
        ('order', '0004_auto_20201128_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='dispatcher',
            field=models.ForeignKey(default=24, on_delete=django.db.models.deletion.PROTECT, to='gde.dispatcher'),
            preserve_default=False,
        ),
    ]
