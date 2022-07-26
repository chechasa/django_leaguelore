# Generated by Django 4.0.5 on 2022-07-14 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lore', '0003_remove_stats_champion_champion_stats_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stats',
            name='armor',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stats',
            name='armor_per_level',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stats',
            name='attack_damage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stats',
            name='attack_damage_per_level',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stats',
            name='attack_range',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stats',
            name='attack_speed',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stats',
            name='attack_speed_per_level',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stats',
            name='hp',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stats',
            name='hp_per_level',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stats',
            name='hp_regen',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stats',
            name='hp_regen_per_level',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stats',
            name='move_speed',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stats',
            name='mp',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stats',
            name='mp_per_level',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stats',
            name='mp_regen',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stats',
            name='mp_regen_per_level',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stats',
            name='spell_block',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stats',
            name='spell_block_per_level',
            field=models.FloatField(),
        ),
    ]
