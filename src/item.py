class Item:
    def __init__(self, name, description, damage, id):
        self.name = name
        self.description = description
        self.damage = damage
        self.id = id

    def __str__(self):
        return (f"\n{self.name},\n{self.description}")