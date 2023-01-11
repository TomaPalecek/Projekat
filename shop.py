import random
from main_menu import *


def shop():
    from base_material import shredder, stinger, screamer, protagonist, zarek

    print("""\n    After continuing down the street I come up on an interesting looking store called \"Zareks Spice Emporium\"
    Zarek's Spice Emporium looks like a vibrant and lively place. The storefront is painted a bright, sunny yellow, 
    and the windows are adorned with colorful displays of spices and cooking ingredients. The sign above the door is painted
    with swirling, bold letters, and it reads "Zarek's Spice Emporium: The Finest Ingredients from Around the Galaxy."
    
    Despite the cheerful appearance of the shop, there is a hint of seediness to it as well. The paint on the storefront is 
    chipped and faded in places, and the windows are a bit grimy. The door is slightly off its hinges, and it creaks loudly 
    as it opens and closes. The storefront is located in a busy, crowded market street, and there is a constant stream of 
    people coming and going. Some of them seem to be there for the spices and ingredients, 
    while others seem to be there for other, more shadowy purposes.
    
    I enter the shop and the shopkeeper that, I assume, is named Zarek is turned away humming a melody while arranging some
    signs.
    """)

    def steal_coins():
        success_chance = 0.65
        if random.random() <= success_chance:
            print("You successfully steal 500 coins!")
            protagonist.add_coins(500)
        else:
            print("Zarek blasts you in the face with his disintegration.\nGame Over")
            quit()

    def dialogue(zarek):
        print(f"""
    Zarek: "Welcome to my shop, my friend! Can I interest you in some of the finest spices and ingredients from around the 
            galaxy?"
    
    {protagonist.name}: "Thanks for the offer, but I'm not in the market for spices right now. Actually, I'm looking for something... 
                        specific. Do you have any rare cooking ingredients or spices that might be hard to come by?"
    
    Zarek: "Well, I do have a few items that might interest you. Follow me to the back."
    
    I cautiously follow him. He seems too easy going for such a trade.
    
    Zarek: "Look, I'm not the one to make deals with just anyone, but I had a good feeling since you stepped foot
            in the shop. And I always trust my gut. Plus, you seem familiar for some reason. Do I know you from somewhere?"
    
    {protagonist.name}: "I get that alot, but we haven't met before. I'm new in town."
    
    Zarek gives you a suspicious look and turns to a leather chest. He opens it and inside is a selection of weapons each
    one deadlier than the last.
    
    Zarek: "This is what I have on hand right now. But hey, don't make me regret trusting you. You don't want me as an 
            enemy, especially if your new here.
            
    {protagonist.name}: "Thanks for the tip, I'll keep that in mind."
    """)
        shop(zarek)
        return

    def shop(zarek):
        choice2 = ""
        while choice2 != "0":
            choice2 = input("He runs me through my options, and explains them briefly.\n"
                            f"1. {shredder.name} - {shredder.description}\n"
                            f"    {shredder.damage} Damage, {shredder.price} coins\n"
                            f"2. {stinger.name} - {stinger.description}\n"
                            f"    {stinger.damage} Damage, {stinger.price} coins\n"
                            f"3. {screamer.name} - {screamer.description}\n"
                            f"    {screamer.damage} Damage, {screamer.price} coins\n"
                            "0. I don't want to buy anything right now.\n"
                            "Zarek: So which one is it?\n"
                            "\nPick the number of the gun you want to buy: "
                            )
            if choice2 == "1":
                if protagonist.coins >= shredder.price:
                    zarek.remove_from_inventory(shredder)
                    protagonist.set_weapon(shredder)
                    protagonist.add_to_inventory(shredder)
                    protagonist.subtract_coins(shredder.price)
                    zarek.add_coins(shredder.price)
                    print(f"{shredder.name} has been added to your inventory.")
                else:
                    print(f"\nI don't have enough coins to purchase {shredder.name}")
            elif choice2 == "2":
                if protagonist.coins >= stinger.price:
                    zarek.remove_from_inventory(stinger)
                    protagonist.set_weapon(stinger)
                    protagonist.add_to_inventory(stinger)
                    protagonist.subtract_coins(stinger.price)
                    zarek.add_coins(stinger.price)
                    print(f"{stinger.name} has been added to your inventory.")
                else:
                    print(f"\nI don't have enough coins to purchase {stinger.name}")
            elif choice2 == "3":
                if protagonist.coins >= screamer.price:
                    zarek.remove_from_inventory(screamer)
                    protagonist.set_weapon(screamer)
                    protagonist.add_to_inventory(screamer)
                    protagonist.subtract_coins(screamer.price)
                    zarek.add_coins(screamer.price)
                    print(f"{screamer.name} has been added to your inventory.")
                else:
                    print(f"\nI don't have enough coins to purchase {screamer.name}")
            elif choice2 == "0":
                return

            else:
                print("Choose a valid option.")

    while True:
        choice = input("I should...\n"
                       "A. Steal the coins on the counter while Zarek isn't looking (65% success chance).\n"
                       "B. Look at the room in the back.\n"
                       "C. Talk to Zarek.\n"
                       "X. Exit the shop\n"
                       "M. Main Menu\n"
                       "Choose an option: ").upper()
        if choice == "A":
            steal_coins()

        elif choice == "B":
            print("\nI sneak a peak through the curtain covering the door and see ammunition and some pulsating orbs that "
                  "remind me of power cores of some kind. There is definitely something more to this shop than spices!\n")

        elif choice == "C":
            dialogue(zarek)

        elif choice == "M":
            main_menu()

        elif choice == "X":
            from entrance import entrance
            entrance()
