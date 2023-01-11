class Weapon:
    def __init__(self, name: str, description: str, damage: int, price: int):
        self.name = name
        self.description = description
        self.damage = damage
        self.price = price

    def __str__(self):
        return f"{self.name}"
