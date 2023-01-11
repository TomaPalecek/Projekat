import random
from base_material import protagonist, big_boss
from character import Character


def combat(protagonist: Character, enemy: Character):
    while protagonist.get_hp() > 0 and enemy.get_hp() > 0:
        print("Attack or run? ")
        action = input().lower()
        if action == "attack":

            if protagonist.weapon == 0:
                print("You don't have a weapon equipped!")
            else:
                protagonist.attack(enemy)
                print(f"I hit him for {protagonist.weapon.damage}")

            if enemy.get_hp() <= 0:
                print("He's down and out...")
                from final_scene import final_scene
                final_scene()

            else:
                print(f"The {enemy.name}'s remaining health is {enemy.get_hp()}")
        elif action == "run":
            print("Big Boss: YOU DON'T GET TO RUN AWAY!!")
            enemy.attack(protagonist)
            print(f"The {enemy.name} attacks you for {enemy.weapon.damage}")

        else:
            print("Enter a valid option.")
        enemy.attack(protagonist)
        print(f"The {enemy.name} attacks you for {enemy.weapon.damage}")
        if protagonist.get_hp() <= 0:
            print("You died.\nGame over.")
            quit()
        else:
            print(f"You have {protagonist.get_hp()} remaining.")


def chandelier_drop():
    success_chance = 0.70
    if random.random() <= success_chance:
        print("The chandelier drops directly onto Big Boss, slamming into his head.\n"
              "He stands up furiously ready to fight.\n")
        big_boss.reduce_hp(100)

    else:
        print("Big Boss notices the chandelier dropping and slaps it away into the wall breaking it from the violent "
              "impact. He takes his weapon and turns to fight you.\n")

    combat(protagonist, big_boss)


def tusk_fling():
    success_chance = 0.50
    if random.random() <= success_chance:
        print("The tusk flies rapidly through the throne stabbing the Big Boss in the arm."
              " He screams in rage and gets his weapon. ")
        big_boss.reduce_hp(150)

    else:
        print("After shooting the tusk it falls clumsily on the ground. The Big Boss jumps from his throne, arms himslef"
              " and gets ready to fight.")

    combat(protagonist, big_boss)

def final_boss():

    print("""
        The inside of the castle is opulent and grand. The floors are made of gleaming marble with red carpets, and 
        the walls are adorned with elaborate tapestries and gold-leafed frescoes. The halls are wide and spacious, 
        with high ceilings and tall windows that let in streams of sunlight. The furniture is made of the finest 
        materials and finished with intricate details. It is clear that this castle is the home of someone with  
        immense wealth and power. The air is filled with the sound of soft music and the gentle rustle of fabrics as 
        servants bustled about their duties. It is a place of grandeur and luxury.
        
        Then I see him as I turn a corner and reflexively fling back behind it. It's Big Boss. He is a giant, 
        olive-colored alien. He is seated on a throne of gold, eating violently. His face is contorted into a permanent 
        scowl, and his small, beady eyes seem to be constantly scanning the room for any sign of disobedience. Despite 
        his immense size, he exudes a sense of power and authority, and it is clear that he is not to be trifled with.\n
    """)

    while True:
        choice = input("A. Look at food.\n"
                       "B. Look at staff.\n"
                       "C. Look at chandelier\n"
                       "D. Look at mammoth head.\n"
                       "E. Attack Big Boss\n"
                       "M. Main Menu\n"
                       "Choose an option: ").upper()

        if choice == "A":
            print("""
        Big Boss is greedily shoveling spoonfuls of a thick, purple goo into his mouth. As he eats, bits of the goo 
        splatter onto the table and floor, staining the white marble with bright splotches of color. The food itself 
        smells pungent and musky, and seems to have bits of some unidentifiable meat mixed in. Despite the mess he is
        making, Big Boss didn't seem to care, focused only on satisfying his insatiable appetite. \n""")

        elif choice == "B":
            print("""
        The staff, a group of timid looking aliens, cautiously move around the room attending to various tasks, keeping 
        their distance from their boss. Only one staff member is near the Big Boss cleaning instantly the stains of his
        disgusting eating. They will flee at the first sign of trouble.\n""")

        elif choice == "C":

            print(f"""
        Hanging above Big Boss is a grand chandelier, sparkling and dazzling in the dimly lit room. It appears to be 
        made of some sort of metallic crystal, with intricate designs etched into its surface. I can probably shoot
        the chandelier and make it fall onto him.\n""")

            shoot_chandelier = input("Shoot the chandelier initiating the fight? 70% success chance - 100 damage."
                                     "Y/N: ").upper()

            if shoot_chandelier == "Y":
                chandelier_drop()

        elif choice == "D":
            print(f"""
            Behind the throne, mounted on the wall, is a stuffed mammoth head. Its tusks are pointed upwards, almost as if 
            challenging me to a duel. I realizes that if I were to shoot the mammoth head, the force of the blast might send
            one of the tusks flying towards Big Boss.\n""")

            shoot_tusk = input("Shoot the tusk initiating the fight? 50% success chance - 150 damage."
                                     "Y/N: ").upper()

            if shoot_tusk == "Y":
                tusk_fling()

        elif choice == "E":
            combat(protagonist, big_boss)

        elif choice == "M":
            from main_menu import main_menu
            main_menu()