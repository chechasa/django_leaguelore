# Generated by Django 4.0.5 on 2022-07-18 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lore', '0016_allytip_enemytip_remove_champion_tip_delete_tip_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='champion',
            name='allytip',
        ),
        migrations.RemoveField(
            model_name='champion',
            name='enemytips',
        ),
    ]
