""" 

Your choice at each step of the game determines what you see next and the options you have available at that point.
You are walking through a dark forest and find two items: a Axe and a Battery. Which one do you want to pick up?

Axe:
    A powerful tool to have. What do you choose next?

    A1> chop wood
            You have many uses for it. What do you make first? 
            A1.2> Shelter
                a pack of wolves approches. you do not make it out of the forest.
            A1.3> Fire
                congratulations, you survive the night.
                
    A2> search cave.
            You found a cave! Good news. However, a wolf jumps out and stares at you.
            A2.1> you fight
                    A brave decision! You win the fight and the wool keeps you warm. You survive the night.
            A2.2> you stay still
                    The wolf jumps you. You do not make it out of the forest.



Batteries:
	An interesting choice to make. What do you do next?

	B1> Use the battery to power up your flashlight 
            A fine choice, you can now see through the dark forest. What do you choose to do next?
            B1.1> Look for a cabin
                You managed to find a cabin to spend the night. You survive the night.                
            B1.2> Search for food
                You find a rabbit but a black bear jumps out of a bush and attacks you both. You do not make it out of the forest.

	B2> Use aluminum wrapping to start a fire.
            Congratulations, you are now warm and safe from the cold. But the smoke attracts savage goblins. What next?
            B2.1> You hide
                    Congratulations. The goblins were not friendly. You survive the night.
            B2.2> You attempt to befriend them
                    As you approach the goblins, they attack you. You do not make it out of the forest.                 
	
"""



one = input(
    "You are walking through a dark forest and find two items: a Axe and a Battery. Which one do you want to pick up? [AXE or BATTERY] > "
)

one = one.lower().strip()

if one.lower() == "axe" or one == '1':
    print("A powerful tool to have. What do you choose next?")
    print(">chop WOOD [1]")
    print(">search for a CAVE [2]")
    wood_or_cave = input("> ").lower().strip()

    # choosing to chop wood
    if wood_or_cave == "1" or wood_or_cave.lower() == 'wood':
        print("Wise decision, many are the uses for this valuable item. What do you choose to make? ")
        print(">SHELTER [1]")
        print(">FIRE [2]")
        shelter_or_fire = input("> ").lower().strip()

        if shelter_or_fire == "1" or shelter_or_fire.lower() == 'shelter':
            print("A pack of wolves approches as you are building your shelter. Unfortunately, you do not make it out of the forest!")
        else:
            print(
                "You manage to keep warm, and Savage Goblins that smell smoke were just out of range. Congratulations, you survive the night."
            )

    # choosing to search cave
    elif wood_or_cave == "2" or wood_or_cave.lower() == 'cave':
        print(
            " You found a cave! Good news. However, a wolf jumps out and stares at you."
        )
        print("What do you decide to do next?")
        print(">You FIGHT. [1]")
        print(">You STAY still. [2]")
        fight_or_staystill = input("> ").lower().strip()

        if fight_or_staystill == "1" or fight_or_staystill.lower() == 'fight':
            print(
                "A brave decision! You win the fight and the wool keeps you warm. You survive the night."
            )
        else:
            print("The wolf jumps you. You do not make it out of the forest.")
    else:
        print("Invalid command. Please try again!")

elif one.lower() == "battery" or one == '2':
    print("An interesting choice. What do you do next?")
    print(">Use the battery to power up your FLASHLIGHT. [1]")
    print(">Use aluminum wrapping to start a FIRE. [2]")
    flashlight_or_fire = input('> ').lower().strip()

    if flashlight_or_fire == '1' or flashlight_or_fire.lower() == 'flashlight':
        print('A fine choice, you can now see through the dark forest. What do you choose to do next?')
        
        print('>Look for a CABIN. [1]')
        print('>Search for FOOD. [2]')
        cabin_or_food = input('> ').lower().strip()

        if cabin_or_food == '1' or cabin_or_food.lower() == 'cabin':
            print('You managed to find a cabin. You survive the night!')    
            
        elif cabin_or_food == '2' or cabin_or_food.lower() == 'food':
            print('You found a rabbit! However, a black bear jumps out of a bush and attacks you both. You do not make it out of the forest.')
        else:
            print('Invalid command. Please try again!')
    
    elif flashlight_or_fire == '2' or flashlight_or_fire.lower() == 'fire':
        print('Congratulations, you are now warm and safe from the cold. But the smoke attracts savage goblins. What next?')
        print('You HIDE. [1]')
        print('You attempt to BEFRIEND them. [2]')
        hide_or_befriend = input('> ').lower().strip()

        if hide_or_befriend == '1' or hide_or_befriend.lower() == 'befriend':
            print('Good choice! The goblins were not friendly. You survive the night!')

        elif hide_or_befriend == '2' or hide_or_befriend == 'befriend':
            print('As you approach the goblins, they attack you. You do not make it out of the forest.')
        
        else:
            print('Invalid command. Please try again.')
    else:
        print('Invalid command. Please try again!') 
    
else:
    print('Invalid command. Please try again!')            


### Extra mile: 
# Adding an option to choose by typing a number to represent each answer
# Trying to handle unexpected choices with an ~invalid command!~ prompt for the user 

