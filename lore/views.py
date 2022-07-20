from ast import Pass
from msilib.schema import Error
from tkinter import E
from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import Champion, Stats, Tag, AllyTip, EnemyTip, Abilities
import json
import requests
# Create your views here.

class Index(View):
    
    def post_into_db(self, request):
        # with open("static/champions.json") as file:
        #    data = json.load(file)["data"]
        # for k, v in data.items():
        if Stats.objects.all():
            pass
                   
        else:
                
            with open("static/champions_by_id.json") as file:
                names = json.load(file)
                for name in names:
                    response = requests.get(f"https://ddragon.leagueoflegends.com/cdn/12.13.1/data/en_US/champion/{name}.json")
                    response = response.json()
                    info = response["data"][name]["stats"]
                    v = response["data"][name]
                    champion = name
                    if name == "Belveth":
                        continue
                    

        #Tag model
                    tags = v["tags"]
                    clean_tags = []
                    for tag in tags:
                        clean_tags += Tag.objects.filter(tag_name=tag)
                    
        #Champion model
                    title = v["title"]
                    blurb = v["blurb"]
                    partype = v["partype"]
                    champion_id = v["key"]
                    lore = v['lore']

        #Stats model
                    hp = info["hp"]
                    hpperlevel = info["hpperlevel"]
                    mp = info["mp"]
                    mpperlevel = info["mpperlevel"]
                    movespeed = info["movespeed"]
                    armor = info["armor"]
                    armorperlevel = info["armorperlevel"]
                    spellblock = info["spellblock"]
                    spellblockperlevel = info["spellblockperlevel"]
                    attackrange = info["attackrange"]
                    hpregen = info["hpregen"]
                    hpregenperlevel = info["hpregenperlevel"]
                    mpregen = info["mpregen"]
                    mpregenperlevel = info["mpregenperlevel"]
                    crit = info["crit"]
                    critperlevel = info["critperlevel"]
                    attackdamage = info["attackdamage"]
                    attackdamageperlevel = info["attackdamageperlevel"]
                    attackspeedperlevel = info["attackspeedperlevel"]
                    attackspeed = info["attackspeed"] 
        #Tips models
                    for tip in response["data"][name]["allytips"]:
                        t = AllyTip(name=champion, allytips=tip)
                        t.save()
                    
                    for tip in response["data"][name]["enemytips"]:
                        t = EnemyTip(name=champion, enemytips=tip)
                        t.save()


        #Abilities model
                    spell_Q = response["data"][name]["spells"][0]
                    spell_W = response["data"][name]["spells"][1]
                    spell_E = response["data"][name]["spells"][2]
                    spell_R = response["data"][name]["spells"][3]

                    ab = Abilities(name=champion, Q_name=spell_Q["name"], Q_cooldown=spell_Q["cooldown"], Q_description=spell_Q["description"], W_name=spell_W["name"], W_cooldown=spell_W["cooldown"], W_description=spell_W["description"],
                     E_name=spell_E["name"], E_cooldown=spell_E["cooldown"], E_description=spell_E["description"], R_name=spell_R["name"], R_cooldown=spell_R["cooldown"], R_description=spell_R["description"])
                    ab.save()

                    if not Stats.objects.filter(champion_name=champion):
                        stats_model = Stats(hp=hp, hp_per_level=hpperlevel, mp=mp, mp_per_level=mpperlevel, move_speed=movespeed, armor=armor, armor_per_level=armorperlevel, spell_block=spellblock,
                        spell_block_per_level=spellblockperlevel, attack_range=attackrange, hp_regen=hpregen, hp_regen_per_level=hpregenperlevel, mp_regen=mpregen, mp_regen_per_level=mpregenperlevel,
                        attack_damage=attackdamage, attack_damage_per_level=attackdamageperlevel, attack_speed_per_level=attackspeedperlevel, attack_speed=attackspeed, champion_name=champion)
                        stats_model.save()
                    cleaned_stats = []
                    cleaned_stats += Stats.objects.filter(champion_name=champion)
                    cleaned_stats = cleaned_stats[0]
                    if not Champion.objects.filter(name=champion):
                        champion_model = Champion(name=champion, title=title ,blurb=blurb ,partype=partype , champion_id=champion_id , stats=cleaned_stats, lore=lore)
                        champion_model.save()
                        for t in clean_tags:
                            champion_model.tags.add(t)





    def get(self, request):
        self.post_into_db(request)
        return render(request, "lore/index.html", context={
            "stats" : Stats.objects.all().order_by("champion_name"),
            "champions" : Champion.objects.all(),
        })


class ChampionDetails(View):
    def get(self, request, slug):      
        champ = get_object_or_404(Champion, slug=slug)
        allytip = AllyTip.objects.filter(name=champ.name)
        enemytip = EnemyTip.objects.filter(name=champ.name)
        ab = get_object_or_404(Abilities ,name=champ.name)
        return render(request, "lore/champion_detailed_page.html", context={
            "champion": champ,
            "allytips": allytip,
            "enemytips": enemytip,
            "ability": ab,
        })
