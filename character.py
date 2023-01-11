from typing import List
from weapon import Weapon
from armor import Armor


class Character:
    def __init__(self, name: str, health: int, coins: int, inventory: List, weapon: Weapon = 0, odds_and_evens_wins=0,
                 thug_defeated=False, armor: Armor = 0):
        self.name = name
        self.health = health
        self.coins = coins
        self.weapon = weapon
        self.armor = armor
        self.thug_defeated = thug_defeated
        self.odds_and_evens_wins = odds_and_evens_wins
        self.inventory = inventory or []

    def __str__(self):
        return f"{self.name} (health: {self.health}, coins: {self.coins}, weapon: {self.weapon}, armor: {self.armor})"

    def get_hp(self):
        return self.health

    def set_hp(self, new_hp_value):
        self.health = new_hp_value

    def set_coins(self, new_coins_value):
        self.coins = new_coins_value

    def set_name(self, new_name):
        self.name = new_name

    def set_weapon(self, new_weapon):
        self.weapon = new_weapon

    def subtract_coins(self, subtraction_value):
        self.coins -= subtraction_value

    def add_coins(self, new_value):
        self.coins += new_value
        print(f"{new_value} coins have been added. You now have {self.coins}")

    def add_to_inventory(self, new_item):
        self.inventory.append(new_item)

    def remove_from_inventory(self, item_to_remove):
        self.inventory.remove(item_to_remove)

    def add_wins(self):
        self.odds_and_evens_wins += 1

    def equip_armor(self, armor: Armor):
        self.health += armor.additional_hp
        print(f"Your health is increased by {armor.additional_hp}. You now have {self.health}\n")

    def attack(self, enemy: "Character"):
        enemy.set_hp(enemy.get_hp() - self.weapon.damage)

    def reduce_hp(self, ammount_to_reduce: int):
        self.health -= ammount_to_reduce

    def __getstate__(self):
        if self.weapon == 0 and self.armor == 0:
            return {'name': self.name, "health": self.health, "coins": self.coins,
                    "odds_and_evens_wins": self.odds_and_evens_wins, "thug_defeated": self.thug_defeated}

        elif self.weapon == 0:
            return {'name': self.name, "health": self.health, "coins": self.coins,
                    "odds_and_evens_wins": self.odds_and_evens_wins, "thug_defeated": self.thug_defeated,
                    "armor_name": self.armor.name,
                    "armor_description": self.armor.description, "armor_bonus_hp": self.armor.additional_hp}
        elif self.armor == 0:
            return {'name': self.name, "health": self.health, "coins": self.coins,
                    "odds_and_evens_wins": self.odds_and_evens_wins, "thug_defeated": self.thug_defeated,
                    'weapon_name': self.weapon.name, 'weapon_damage': self.weapon.damage,
                    "weapon_description": self.weapon.description, "weapon_price": self.weapon.price}
        else:
            return {'name': self.name, "health": self.health, "coins": self.coins,
                    "odds_and_evens_wins": self.odds_and_evens_wins, "thug_defeated": self.thug_defeated,
                    'weapon_name': self.weapon.name, 'weapon_damage': self.weapon.damage, "armor_name": self.armor.name,
                    "armor_description": self.armor.description, "armor_bonus_hp": self.armor.additional_hp,
                    "weapon_description": self.weapon.description, "weapon_price": self.weapon.price}

    def __setstate__(self, state):

        self.name = state['name']
        self.health = state['health']
        self.coins = state['coins']
        self.odds_and_evens_wins = state['odds_and_evens_wins']
        self.thug_defeated = state['thug_defeated']

        if 'weapon_name' in state and 'weapon_damage' in state and "armor_name" in state and "armor_description" in state \
                and "armor_bonus_hp" in state and "weapon_description" in state and "weapon_price" in state:

            self.weapon = Weapon(state['weapon_name'], state["weapon_description"], state['weapon_damage'], state["weapon_price"])
            self.armor = Armor(state["armor_name"], state["armor_description"], state["armor_bonus_hp"])

        elif 'weapon_name' in state and 'weapon_damage' in state and "weapon_description" in state and "weapon_price" in state:

            self.weapon = Weapon(state['weapon_name'], state["weapon_description"], state['weapon_damage'], state["weapon_price"])
            self.armor = 0
        elif "armor_name" in state and "armor_description" in state and "armor_bonus_hp" in state:
            self.weapon = 0
            self.armor = Armor(state["armor_name"], state["armor_description"], state["armor_bonus_hp"])
        else:
            self.weapon = 0
            self.armor = 0
