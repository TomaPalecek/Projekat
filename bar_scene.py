def bar_scene():
    from base_material import protagonist, titanium_breastplate, note_to_zarek, the_bartender

    print("""
        I walked into the dimly lit bar. It's mostly empty, only consisting of the ones I bet spend more time inside the
        bar than out. I start scanning the room from corner to corner.\n """)

    while True:
        choice = input("A. Look at the bar.\n"
                       "B. Look at drunk aliens.\n"
                       "C. Approach the bar\n"
                       "D. Approach a lone drunk alien.\n"
                       "E. Leave the bar.\n"
                       "M. Main Menu\n"
                       "Choose an option: ").upper()

        if choice == "A":
            print("""
        There are two bartender in shift. One a big, rotund alien tending the bar, his skin a deep purple hue and small
        one the size of an owl tending to the dishes and taps.\n""")

        elif choice == "B":
            print("""
        I can't help but notice the various alien patrons scattered throughout the room. Some are hunched over their 
        drinks, muttering to themselves in slurred speech. Others are boisterously singing and laughing, clearly well 
        beyond their limits. I shake my head at the sight of these poor creatures, wasting their lives away in this 
        dingy establishment.\n
        """)

        elif choice == "C":
            print(f"""
        I walk up to the bar and the purple alien approaches me.
        
        Bartender: What'll it be, stranger?
        
        I order a drink and we begin chatting. We introduce ourselves, and his name sounds like a series of guttural 
        noises and what I think are tribal chants. As we talk, he seems to be asking some prying questions inbetween 
        casual ones, then he finally commits.
        
        Bartender: You're here to take down Big Boss, aren't you?
        
        {protagonist.name}: Uhm... Yes, I am, but... How did you know!?
        
        Bartender: Kael dropped by to say goodbye before he left the city. He told me about your interaction at the square.
        Listen to me carefully now, {protagonist.name}. I've got a bone to pick with that scumbag myself. Big Boss banished my 
        family from the wealthy town and left me here to rot. I've been waiting for someone like you to come along and 
        take him down. I want to help.

        The bartender goes to a room in the back and brings back a shiny new set of armor. 
        
        The Bartender: Take this, it's the best I've got. And here, take this note to Zarek. He's a friend and owes
        me one. He'll hook you up with a weapon for free if you show it to him. Good luck on your mission.
        
        {protagonist.name}: I will eliminate him, you will be free to join your family soon enough. Thank you.\n
        """)

            print(f"{titanium_breastplate.name} and a note to zarek has been added to your inventory.")
            protagonist.equip_armor(titanium_breastplate)
            protagonist.inventory.append(titanium_breastplate)
            protagonist.inventory.append(note_to_zarek)
            the_bartender.remove_from_inventory(titanium_breastplate)
            the_bartender.remove_from_inventory(note_to_zarek)

        elif choice == "D":
            print(f"""
        One particularly drunk alien, a slovenly looking creature with multiple tentacles and a bulbous head, calls me over.
        
        Drunk Alien: Hey buddy, come over here for a sec.
        
        {protagonist.name}: What do you want?
        
        Drunk Alien: I need you to do me a favor.
        
        {protagonist.name}: And what's that?
        
        Drunk Alien: I need you to slap me. As hard as you can.
        
        {protagonist.name}: I'm sorry, I'm not into that kind of stuff.
        
        Drunk Alien: It's a tradition in my species. When we get really drunk, we find someone to slap us as hard as they can. It helps sober us up.
        
        {protagonist.name}: That's the most ridiculous thing I've ever heard.
        
        Drunk Alien: Come on, just do it. I promise it's not sexual.
        
        {protagonist.name}: Fine, but you asked for it.
        
        I slap the Drunk Alien. He groans and falls to the ground. As the Drunk Alien hits the ground, he lets out a 
        colossally loud fart and a rapid series of burps. He's knocked out cold. I don't know if its from the slap or the
        fall. 
        
        The other patrons in the bar all start laughing and jeering at the poor alien.
        """)

        elif choice == "E":
            from the_gates import the_gates
            the_gates()

        elif choice == "M":
            from main_menu import main_menu
            main_menu()
