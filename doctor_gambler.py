
def odds_and_evens():
    import random
    from base_material import protagonist, plasma_shield, plasma_cannon, the_doctor

    print("""
    The Doctor: Maybe as an outsider, you heard of this game. It's a simple game of odds and evens. 
    You pick either odd or even, and I'll roll a die. If the number that comes up is odd and you picked odd, 
    or even and you picked even, you win. First to three wins. It's a real hoot, ain't it? 
    Now, what'll it be? Odd or even?\n""")

    choices = ["odd", "even"]
    doctor_score = 0
    player_score = 0

    while doctor_score < 3 and player_score < 3:
        player_choice = ""
        while player_choice != "odd" and player_choice != "even":
            player_choice = input("odd or even? ")
            if player_choice != "odd" and player_choice != "even":
                print("Please choose odd or even: ")
        doctor_choice = choices[0] if player_choice == choices[1] else choices[1]
        print(f"You are {player_choice} and the doctor is {doctor_choice}.\n")
        random_number = random.randint(1, 6)
        print(f"The doctor throws a {random_number}.")
        if (random_number % 2 == 0 and player_choice == "even") or (random_number % 2 != 0 and player_choice == "odd"):
            player_score += 1
            print(f"You win this round! The score is {player_score} to {doctor_score}\n")
        else:
            doctor_score += 1
            print(f"The doctor wins this round. The score is {player_score} to {doctor_score}\n")

    if player_score == 3:
        protagonist.add_wins()
        print(f"""
        The Doctor: Gosh darn it! Well feller... You beat me fair and square. What do ya want to have done?

        {protagonist.name}: What do you mean?

        The Doctor: People play with me to get a free surgical modification. Ya know, laser eyes, shark teeth and what not.

        {protagonist.name}: Yeah, I'm not interested in that. The game was enjoyable enough. Thank you!

        The Doctor: Now hold on just a minute! Don't give me that humble smug crap. I play these games for the thrill
        of the gamble, you ain't taking that away from me.\n""")

        if protagonist.odds_and_evens_wins == 1:
            print("""The Doctor gave me 600 coins. Wow. What a character.\n""")
            protagonist.add_coins(600)

            return

        if protagonist.odds_and_evens_wins == 2:
            print(f"""The Doctor gave me {plasma_shield.name}.\n""")
            protagonist.equip_armor(plasma_shield)
            protagonist.inventory.append(plasma_shield)
            the_doctor.remove_from_inventory(plasma_shield)

            return

        if protagonist.odds_and_evens_wins == 3:
            print(f"""The Doctor gave me {plasma_cannon.name}.\n""")
            protagonist.set_weapon(plasma_cannon)
            protagonist.inventory.append(plasma_cannon)
            the_doctor.remove_from_inventory(plasma_cannon)

            return

        else:
            print("""
        The Doctor: Scramble son! I haven't anything else to give you!""")
            return

    else:
        print("The Doctor: HA! Ain't none of y'all stopping my streak!")
    return


def doctor_gambler():

    print("""        As I make your way through the bustling town square, I come across a large group of people huddled 
        around a building on the outskirts of the square. Curious, I approach to get a better look and are about to catch 
        a glimpse of what's going on inside when a stranger suddenly steps in front of you.
    
        Stranger: Ah, I wouldn't recommend getting too close if I were you, That's the local doctor's office and he's 
        got quite the reputation for gambling. There's a high stakes game going on in there right now.
    
        Intrigued, I decide to take a chance and see what's happening. As I push my way through the crowd, 
        I catch a glimpse of the doctor, a tall, thin alien with a sly smile on his face. He seems to be winning,
        and before long the other gambler throws in the towel and storms out of the room. As the doctor counts his 
        winnings, he notices me standing there and gives me a sly wink. 
    
        The Doctor: Well, well, what do we have here? A newcomer to our little town, I see. Fancy a game of chance?
    
        he asks, gesturing to the table in front of him.\n""")

    while True:
        game_choice = input("Do you want to play the game? Y/N: ").upper()

        if game_choice == "Y":
            odds_and_evens()
        elif game_choice == "N":
            from scene_sqaure import scene_square
            scene_square()
        else:
            print("Choose a valid answer.")
