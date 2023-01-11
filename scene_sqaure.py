def alien_interaction():
    from base_material import protagonist
    print(f"""
        {protagonist.name}: Excuse me, I couldn't help but notice you seemed to be lost in thought. Is everything alright?\n
        Kael: Oh, yeah. Sorry about that. Just taking in the square. It's a pretty lively place, isn't it?\n
        {protagonist.name}: Definitely. So, what brings you to this part of town? Do you live around here?\n
        Kael: No, I'm actually from a different part of the planet. I'm just passing through on a delivery for my boss.\n
        {protagonist.name}: Oh, I see. And who is your boss, if you don't mind me asking?\n
        Kael: Oh, it's no big deal. My boss is just this big guy. Goes by the fitting name Big Boss. 
        He's got a pretty tight operation going on here.\n
        {protagonist.name}: Big Boss? I've heard of him. He's quite notorious in these parts.\n
        Kael: Yeah, he's definitely got a reputation. But around here, he's more like a mayor. 
        Everyone in the town sees him as a legitimate businessman, not a crime boss. It's only when you go below to the
        other parts of the planet that you realize what he's really up to.\n
        {protagonist.name}: Interesting. And how did you get involved with him?\n
        Kael: I was just trying to make a little extra credit on the side. I needed the money to send back home to 
        my family. And Big Boss was willing to pay well for someone like me who has a knack for tech. I'm not exactly a
        high-ranking member of his crew or anything, but I do help out as a supply guy. I get orders for various tech
        and other supplies, and deliver them to the crew. I'm just a small cog in the machine.\n
        {protagonist.name}: I see. Well, thanks for the information. Do you know where I could find Big Boss. Some of his 
        usual whereabouts?\n
        Kael: Well, he lives in that big castle over there. But it's heavily guarded and protected. I've never actually
        been inside. I just make my deliveries in the alley next to the castle. That's as close as I've ever gotten.\n
        {protagonist.name}: I appreciate you taking the risk to tell me all of this.\n
        Kael: Listen man, I told you general information that everybody here knows. I don’t know what you’re planning 
        on doing and I don’t wanna know. I made my last delivery and washed my hands clean. 
        I’m heading back to my family in the city below soon and I don’t need Big Boss suspecting anything. 
        All I know is that someone who's going around asking a lot of questions usually gets shut up pretty quickly… 
        I have to go now, good luck with whatever you got going on.
        """)


def scene_square():
    print("""        I get to the cities town square. It's a massive circular plateau with a single column in the 
        center. Creme marble floors with black lightning running through each plate. The square feels empty even though 
        theres about 10 groups populating it. It's hard to imagine it full, being this size.
        
        Surrounding the square, there are the usual highly stylised buildings, a building smaller than the rest but
        with a crowd around it on the west and a single road to the north that leads to a castle-like building. 
        The building clearly stands out from the rest. 
        
        While walking around the square, I notice a lanky looking alien who seems to be as new to the square as I am.
        He looks like he's taking in the sights, sounds and sheer volume of the square. 
            """)

    while True:
        choice = input("What should I invastigate?\n"
                       "A. Talk to the lanky alien.\n"
                       "B. Look at the statue in the middle.\n"
                       "C. Move on from the square\n"
                       "M. Main Menu\n"
                       "Choose an option: ").upper()

        if choice == "A":
            alien_interaction()

        elif choice == "B":
            print("\n       The column stretches about 4m high and has cracks all over it. Feels like it is not from this planet.\n "
                  "       I can see light emiting from some of the deeper cracks. Perhaps it contains some sort of energy.\n")

        elif choice == "C":
            directions = ["north", "east", "south"]
            print(f"Options: {directions}")
            user_input = ""
            while user_input not in directions:
                user_input = input().lower()
                if user_input == "north":
                    from the_gates import the_gates
                    the_gates()
                    pass
                elif user_input == "east":
                    from doctor_gambler import doctor_gambler
                    doctor_gambler()
                elif user_input == "south":
                    from entrance import entrance
                    entrance()
                else:
                    print("Please enter a valid option.")

        elif choice == "M":
            from main_menu import main_menu
            main_menu()