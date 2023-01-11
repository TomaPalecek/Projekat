from weapon import Weapon
from character import Character
from armor import Armor

"""All weapons"""
screamer = Weapon("The Screamer", "A sonic blaster that fires high-frequency sound waves capable of tearing through "
                                  "metal.", 65, 1000)
stinger = Weapon("The Stinger", "A venomous needle gun that injects a deadly poison into its targets.", 50, 750)

disintegrator = Weapon("The Disintegrator", "A powerful energy weapon that vaporizes its targets on contact.", 75, 2000)

shadowblade = Weapon("The Shadowblade", "A stealthy, energy-based sword that can cut through almost anything."
                     , 70, 1750)
frostbite = Weapon("The Frostbite", "A cryogenic cannon that fires blasts of super-cold gas, "
                                    "freezing its targets solid.", 60, 900)
shredder = Weapon("The Shredder", "A rapid-fire machine gun that sprays a hail of bullets at its targets.", 55, 850)

mindfryer = Weapon("The Mindfryer", "A psychic weapon that attacks the mental defenses of its targets, causing "
                                    "confusion and hallucinations.", 40, 2500)

graviton = Weapon("The Graviton", "A weapon that manipulates gravity, capable of crushing its targets with powerful "
                                  "gravitational forces.", 50, 2000)

plasma_cannon = Weapon("The Plasma Cannon", "A heavy weapon that fires blasts of superheated plasma, capable of "
                                            "melting through almost any material.", 75, 5000)

annihilator = Weapon("The Annihilator", "A weapon of mass destruction that generates a miniature black hole, "
                                        "capable of destroying entire planets.", 65, 10000)

"""All Armor"""

plasma_shield = Armor("Plasma Shield", "A high-tech shield that deflects part of the attacks.", 60)
titanium_breastplate = Armor("Titanium Breastplate",
                             "A durable breastplate made of titanium, able to withstand heavy blows.", 75)
energy_absorber = Armor("Energy Absorber", "An advanced suit that absorbs the energy of attacks.", 90)
nanoparticle_suit = Armor("Nanoparticle Suit",
                          "A suit made of nanomachines that repair and strengthen the user's armor in real time.", 120)
tachyon_field_generator = Armor("Tachyon Field Generator", "An experimental suit that creates a tachyon field.", 160)

with open("note_to_zarek.txt", "w") as note_to_zarek:
    note_to_zarek.write("Give him a free weapon or I will pummel you until you can't breathe or see.")

"""All characters"""
protagonist = Character("", 100, 0, [])
zarek = Character("Zarek", 120, 1000, [shredder, stinger, screamer], disintegrator)
the_doctor = Character("The Doctor", 120, 1500, [plasma_shield, plasma_cannon])
the_bartender = Character("The Bartender", 200, 10000, [titanium_breastplate, note_to_zarek])
thug = Character("Thug", 100, 400, [graviton, nanoparticle_suit], graviton)
big_boss = Character("Big Boss", 150, 10000, [tachyon_field_generator, annihilator], annihilator)

"""For saving progress"""
game_state = dict()
game_state["characters"] = [protagonist, zarek, the_bartender, the_doctor, thug, big_boss]
game_state["current_scene"] = ""  # Not utilised

