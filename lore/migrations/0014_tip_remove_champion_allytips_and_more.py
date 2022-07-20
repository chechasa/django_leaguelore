# Generated by Django 4.0.5 on 2022-07-18 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lore', '0013_champion_allytips_champion_enemytips'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('allytips', models.TextField()),
                ('enemytips', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='champion',
            name='allytips',
        ),
        migrations.RemoveField(
            model_name='champion',
            name='enemytips',
        ),
    ]