# Generated by Django 4.0.5 on 2022-07-13 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lore', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='champion',
            name='stats',
        ),
        migrations.AddField(
            model_name='stats',
            name='champion',
            field=models.ManyToManyField(to='lore.champion'),
        ),
    ]
