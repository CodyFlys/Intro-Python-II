from room import Room
from player import Player
from item import Item
import sys
import time

# Declare all the rooms

room = {

    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

player = Player(
    current_room = room['outside'],
    name = "Ducky"
)

item = {
    'rusty_sword': Item("Rusty Sword", "An old rusty Sword, It's better than nothing!", 20, 1),
    'silver_sword': Item("Silver Sword", "An old rusty Silver Sword.", 25, 2),
    'shield': Item("Shield", "An old rusty Shield, It may block a few hits.", 5, 3),
    'lantern': Item("Lantern", "A source of light!", 0, 4),
    'letter': Item("Letter", "An old Letter left behind", 0, 5)
}
room['foyer'].addItem(item['silver_sword'])
room['foyer'].addItem(item['rusty_sword'])
room['overlook'].addItem(item['shield'])

print(f"You are outside an unfamiliar place {player.name}, press c to see your controls or q to quit.\n ")
player_input = []

while not player_input == "q":

    if player.current_room.items != []:
        for i in player.current_room.items:
            if player_input == f"take {i.name}":
                player.takeItem(i)
                player.current_room.removeItem(i)
    else:
        if "take" in player_input: 
            print("There is nothing to take.")
            
    player_input = str(input("What will you do?:\n "))

    if player.items != []:
        for i in (player.items):
            print(i)
            if player_input == f"drop {i.name}":
                player.dropItem(i)
    else:
        if "drop" in player_input:
            print("You don't have any items.")

    if player_input == "c":
        print("CONTORLS:\n'w' = Travel North\n'a' = Travel West\n's' = Travel South\n'd' = Travel East\n'r' = Location\n'q' = Quit\n'd' = drop\n'i' = inventory\n")

    if player_input == "r":
        print(player.current_room)

    if player_input == 'i':
        if player.items != []:
            print("Inventory:")
            for i in player.items:
                print(i)
        else:
            print("You have no items!")

    elif player_input == "w":
        if player.current_room.n_to != []:
            player.current_room = player.current_room.n_to
            print(f"You enter the {player.current_room.name}.\n{player.current_room.description}\n")
            if player.current_room.items != []:
                for i in player.current_room.items:
                    print(f"you found {i.name}")
        else:
            print("You can't go that way!")

    elif player_input == "d":
        if player.current_room.e_to != []:
            player.current_room = player.current_room.e_to
            print(f"You enter the {player.current_room.name}.\n{player.current_room.description}\n ")
            if player.current_room.items != []:
                for i in player.current_room.items:
                    print(f"you found {i.name}")
        else:
            print("You can't go that way!")

    elif player_input == "s":
        if player.current_room.s_to != []:
            player.current_room = player.current_room.s_to
            print(f"You enter the {player.current_room.name}.\n{player.current_room.description}\n ")
            if player.current_room.items != []:
                for i in player.current_room.items:
                    print(f"you found {i.name}")
        else:
            print("You can't go that way!")

    elif player_input == "a":
        if player.current_room.w_to != []:
            player.current_room = player.current_room.w_to
            print(f"You enter the {player.current_room.name}.\n{player.current_room.description}\n ")
            if player.current_room.items != []:
                for i in player.current_room.items:
                    print(f"you found {i.name}")
        else:
            print("You can't go that way!")










#     if player_input == "w":
#         player.current_room = room["foyer"]
#         print("You enter the foyer")
    
#     if player_input == "a":
#         print("There is nothing of interest to your left")

#     if player_input == "s":
#         print("There is nothing of interest behind you")

#     if player_input == "d":
#         print("There is nothing of interest to your right")


# if player_input == "q":
#     sys.exit()