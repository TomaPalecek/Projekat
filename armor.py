class Armor:

    def __init__(self, name: str, description:str, additional_hp: int):
        self.name = name
        self.description = description
        self.additional_hp = additional_hp

    def __str__(self):
        return f"{self.name}"
