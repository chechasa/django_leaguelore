# Generated by Django 4.0.5 on 2022-07-19 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lore', '0017_remove_champion_allytip_remove_champion_enemytips'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('Q_name', models.CharField(max_length=40)),
                ('Q_cooldown', models.CharField(max_length=25)),
                ('Q_description', models.TextField()),
                ('W_name', models.CharField(max_length=40)),
                ('W_cooldown', models.CharField(max_length=25)),
                ('W_description', models.TextField()),
                ('E_name', models.CharField(max_length=40)),
                ('E_cooldown', models.CharField(max_length=25)),
                ('E_description', models.TextField()),
                ('R_name', models.CharField(max_length=40)),
                ('R_cooldown', models.CharField(max_length=25)),
                ('R_description', models.TextField()),
            ],
        ),
    ]