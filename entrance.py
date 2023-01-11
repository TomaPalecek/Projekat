def entrance():

    print("""I find myself at a crossroad, at this point any direction will make me more familiar with the town, 
but I think I'll go: """)

    directions = ["north", "west"]
    user_input = ""

    while user_input not in directions:

        print(f"Options: {directions}")
        user_input = input().lower()

        if user_input == "north":
            from scene_sqaure import scene_square
            scene_square()

        elif user_input == "west":
            from shop import shop
            shop()

        else:
            print("Please enter a valid option.")
