def the_gates():
    from base_material import protagonist
    print("""
        I walk up to the entrance of the castle and try to scope it out.
    """)

    while True:
        choice = input("Wonder what I should do next...\n"
                       "A. Look at castle gates.\n"
                       "B. Approach the gates.\n"
                       "C. Sneak through the gates\n"
                       "D. Move on from the castle entrance.\n"
                       "M. Main Menu\n"
                       "Choose an option: ").upper()

        if choice == "A":
            print("""
        As I look closer, I notice that the gates are guarded by a group of heavily armed soldiers. They stand 
        at attention, their armor gleaming in the sunlight. It's clear that they are not to be trifled with.
        I hesitate for a moment, wondering if I should try to sneak past them or if I should just turn back now. 
        
        I see the alley that the lanky alien told me about on the west and something that looks like this planets version of
        a bar to the east of these gates.\n""")

        elif choice == "B":
            print("""
        As I approach the gates of the castle, I am struck by their imposing presence. They tower above me, made of a sleek,
        metallic material that shimmers in the sunlight. It's clear that this is no ordinary castle - it looks more like a 
        futuristic fortress. 
        
        I can't make out a safe way to go into the premises without being detected. Plus, I don't know Xanthes technology,
        who knows what detection systems they have integrated into the gates and beyond.
        
        Before I can inspect any more, one of the guards asks me to keep moving.\n""")

        elif choice == "C":

            print(f"""
        {protagonist.name} decides to try and sneak past them in order to find Big Boss, but one of the guards 
        spots him and calls out. The protagonist tries to run, but the guards catch up and strike him down with 
        their weapons. As he takes his last breath, he realizes that he has failed in his mission to bring down 
        Big Boss.
        """)
            print("Game Over")
            quit()

        elif choice == "D":
            directions = ["north", "east", "west", "south"]
            print(f"Options: {directions}")
            user_input = ""
            while user_input not in directions:
                user_input = input().lower()
                if user_input == "north":

                    print("There is no chance I can go through the front gate.\n")

                elif user_input == "east":
                    from bar_scene import bar_scene
                    bar_scene()

                elif user_input == "west":
                    from alley_scene import alley_scene
                    alley_scene()

                elif user_input == "south":
                    from scene_sqaure import scene_square
                    scene_square()
                else:
                    print("Please enter a valid option.")

        elif choice == "M":
            from main_menu import main_menu
            main_menu()
