from calendar import c
from tabnanny import verbose
from django.db import models
from django.utils.text import slugify

# Create your models here.

class Tag(models.Model):
    tag_name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.tag_name

class Stats(models.Model):
    hp = models.FloatField()
    hp_per_level = models.FloatField()
    mp = models.FloatField()
    mp_per_level = models.FloatField()
    move_speed = models.FloatField()
    armor = models.FloatField()
    armor_per_level = models.FloatField()
    spell_block = models.FloatField()
    spell_block_per_level = models.FloatField()
    attack_range = models.FloatField()
    hp_regen = models.FloatField()
    hp_regen_per_level = models.FloatField()
    mp_regen = models.FloatField()
    mp_regen_per_level = models.FloatField()
    attack_damage = models.FloatField()
    attack_damage_per_level = models.FloatField()
    attack_speed_per_level = models.FloatField()
    attack_speed = models.FloatField()
    champion_name = models.CharField(max_length=50, null=True, unique=True)
    
    class Meta:
        verbose_name_plural = "Stats"

    
    def __str__(self):
        return self.champion_name

class AllyTip(models.Model):
    name = models.CharField(max_length=25)
    allytips = models.TextField()
    def __str__(self) -> str:
        return self.allytips

class EnemyTip(models.Model):
    name = models.CharField(max_length=25)
    enemytips = models.TextField()
    def __str__(self) -> str:
        return self.enemytips

class Abilities(models.Model):
    name = models.CharField(max_length=25)
    Q_name = models.CharField(max_length=40)
    Q_cooldown = models.CharField(max_length=25)
    Q_description = models.TextField()
    W_name = models.CharField(max_length=40)
    W_cooldown = models.CharField(max_length=25)
    W_description = models.TextField()
    E_name = models.CharField(max_length=40)
    E_cooldown = models.CharField(max_length=25)
    E_description = models.TextField()
    R_name = models.CharField(max_length=40)
    R_cooldown = models.CharField(max_length=25)
    R_description = models.TextField()
    

class Champion(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(null=False, db_index=True, blank=True, max_length=100, unique=True)
    title = models.TextField(max_length=300)
    blurb = models.TextField() 
    partype = models.CharField(max_length=25)
    champion_id = models.IntegerField()
    tags = models.ManyToManyField(Tag)
    stats = models.ForeignKey(Stats, on_delete=models.CASCADE, null=True)
    lore = models.TextField(null=True)


    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)




