# Generated by Django 4.0.5 on 2022-07-14 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lore', '0002_remove_champion_stats_stats_champion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stats',
            name='champion',
        ),
        migrations.AddField(
            model_name='champion',
            name='stats',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lore.stats'),
        ),
        migrations.AddField(
            model_name='stats',
            name='champion_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
