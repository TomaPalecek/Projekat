def introduction():
    from base_material import protagonist

    introduction = """
    As I regain access to my senses, I realize that I've crashed in a rocky desert area of my destination, planet Xanthe. 
    My head is throbbing and it takes me a moment to gather my bearings. I must have blacked out after the crash.
    
    I stumble out of my ship and begin to wander through the strangely humid desert, searching for signs of civilization. 
    After what feels like an eternity, I finally spot the outskirts of a city in the distance.
    
    I make my way to the city, taking in my surroundings as I walk. The city is bustling with activity, 
    the streets crowded with all manner of alien species going about their business. 
    I see vendors selling strange, exotic goods, and hear the sounds of music and laughter coming from the various Taverns 
    and Inns scattered throughout the city.
    
    As I walk through the crowded streets, I realize that the inhabitants of this planet are unfamiliar with my face, which 
    is strange since it is plastered all over the galaxy. Best to keep it that way, the mission will be greatly easier. 
    To avoid drawing attention to myself even further, I should use an alias as I explore this strange world. 
    
    """

    print(introduction)
    alias = input("Enter your new alias: ")
    protagonist.set_name(alias)

    print("""\n    I quickly realize that my current suit and weapons are no match for the harsh conditions and dangerous 
    creatures that roam this land. I'll have to find new equipment if I hope to survive on this hostile planet.
    
    My goal is to find and eliminate the notorious crime giant known only as Big Boss. I've heard he's 
    well-equipped and well-guarded, so I'll have to be cunning and resourceful as I search for him.
    
    I'll need to be careful and stay alert. Who knows what dangers this planet holds? But with my training and
    determination, I'm confident I can accomplish my mission and eliminate Big Boss.
    
    Once I emerge from the narrow streets, I see a huge chunk of land elevated from the base level. As if it was cut and 
    pulled out of the ground. There is another city on top, it is unlike the town I've seen so far. It is a blatant separation
    of the rich from the poor. That is where I will most likely find Big Boss.
    
    I make my way to it's base and sneak into a cargo lift. As the elevator ascends I see more of the barren lands and the 
    town bellow becomes smaller and smaller. I turn around as the elevator comes to a stop to see grand and luxurious 
    buildings, with marble columns, gold-plated doors, and sprawling gardens. The streets are lined with exotic plants and 
    flowers, and the air is filled with the scent of jasmine and roses.
    """)
    from entrance import entrance

    entrance()

