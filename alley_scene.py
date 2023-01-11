from base_material import protagonist, graviton, nanoparticle_suit, thug
from character import Character


def combat_won():
    print("\nI can go into the castle and face Big Boss through this backdoor. However, it is guaranteed he will be a "
          "tough fight, I wonder if I have powerful enough equipment to fight him. ")

    while True:
        choice1 = input("A. Go inside the castle and fight Big Boss.\n"
                       "B. Return to the castle gates and find a better loadout.\n"
                       "M. Main Menu\n"
                       "Choose an option: ").upper()
        if choice1 == "A":
            from final_boss import final_boss
            final_boss()
            pass

        elif choice1 == "B":
            from the_gates import the_gates
            the_gates()

        elif choice1 == "m":
            from main_menu import main_menu
            main_menu()


def combat(protagonist: Character, enemy: Character):
    while protagonist.get_hp() > 0 and enemy.get_hp() > 0:
        print("Attack or run? ")
        action = input().lower()
        if action == "attack":

            if protagonist.weapon == 0:
                print("You don't have a weapon equipped!")
            else:
                protagonist.attack(enemy)
                print(f"I hit {enemy.name} for {protagonist.weapon.damage}")

            if enemy.get_hp() <= 0:
                print("He's down and out...")
                return True

            else:
                print(f"The {enemy.name}'s remaining health is {enemy.get_hp()}")
        elif action == "run":
            print(f"You run away from the {enemy.name}.")
            return False
        else:
            print("Enter a valid option.")
        enemy.attack(protagonist)
        print(f"The {enemy.name} attacks you for {enemy.weapon.damage}")
        if protagonist.get_hp() <= 0:
            print("You died.\nGame over.")
            quit()
        else:
            print(f"You have {protagonist.get_hp()} remaining.")


def alley_scene():

    print("""
            I carefully walk through the alleys next to the castle and find a backdoor guarded by one mean looking thug.
        """)
    while True:
        if protagonist.thug_defeated:
            combat_won()

        else:
            choice = input("Should I fight him?\n"
                           f"Yes - Fight the thug with the your current weapon ({protagonist.weapon}) and armor ({protagonist.armor}).\n"
                           "No - Go back to the castles gates.\n"
                           "M. Main Menu\n"
                           "Choose an option: ").lower()

            if choice == "yes":
                starting_hp = protagonist.get_hp()
                if combat(protagonist, thug):
                    protagonist.thug_defeated = True
                    print("I defeat the thug, and grab his loot.\n")
                    print(f"{thug.weapon.name} and {nanoparticle_suit.name} added to your inventory.\nHealth restored "
                          f"to full.")

                    protagonist.set_hp(starting_hp)
                    protagonist.equip_armor(nanoparticle_suit)
                    protagonist.set_weapon(graviton)
                    protagonist.inventory.append(graviton)
                    protagonist.inventory.append(nanoparticle_suit)
                    thug.remove_from_inventory(nanoparticle_suit)
                    thug.remove_from_inventory(graviton)
                    combat_won()

                else:
                    print("Health restored to full.")
                    protagonist.set_hp(starting_hp)
                    from the_gates import the_gates
                    the_gates()

            elif choice == "no":
                from the_gates import the_gates
                the_gates()

            elif choice == "m":
                from main_menu import main_menu
                main_menu()
