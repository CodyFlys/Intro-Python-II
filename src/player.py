# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, items=[], health=100):
        self.current_room = current_room
        self.name = name
        self.items = items
        self.health = health

    def __str__(self):
        return f"current Room: {self.current_room.name}"

    def takeItem(self, item):
        self.items.append(item)
        print(f"You picked up {item}.")
    def dropItem(self, item):
        self.items.remove(item)
        print(f"You dropped {item}.")