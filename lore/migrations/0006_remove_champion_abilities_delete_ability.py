# Generated by Django 4.0.5 on 2022-07-15 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lore', '0005_alter_stats_champion_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='champion',
            name='abilities',
        ),
        migrations.DeleteModel(
            name='Ability',
        ),
    ]
