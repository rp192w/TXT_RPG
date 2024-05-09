from enum import Enum
from collections import defaultdict
from weapon import Weapon, dagger, short_bow, iron_sword, battle_axe, steel_sword, magic_staff, fire_breath, mace
from health_bar import HealthBar, ManaBar
from item import health_potion, mana_potion

class Character:
    def __init__(self, name: str, health: int, maxHealth: int, mana: int, maxMana: int, gold: int = 0) -> None:
        self.name = name
        self._health = health
        self.health_bar = HealthBar(self, maxHealth)
        self.mana = mana
        self.mana_bar = ManaBar(self, maxMana)
        self.maxHealth = maxHealth
        self.gold = 0

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = max(0, min(value, self.maxHealth))
        
    def attack(self, target) -> None:
        damage = self.weapon.attack()
        target.health -= damage
        print(f"{self.name} dealt {damage} damage to {target.name} with {self.weapon.name}")

    def mana_attack(self, target) -> None:
        damage = self.weapon.attack() * 3
        target.health -= damage
        print(f"{self.name} dealt {damage} damage to {target.name} with mana attack")


    def __str__(self):
        return self.name

class Hero(Character):
    def __init__(self, name: str, health: int, maxHealth: int, mana, maxMana) -> None:
        super().__init__(name=name, health=health, maxHealth=maxHealth, mana=mana, maxMana=maxMana)
        self.weapon = dagger
        self.default_weapon = self.weapon
        self.maxHealth = maxHealth
        self.maxMana = maxMana
        self.inventory = [dagger]
        self.item_inventory = {health_potion: 0, mana_potion: 0}
        self.health_bar = HealthBar(self, color="green")

    def equip(self, weapon) -> None:
        if isinstance(weapon, Weapon):
            print(f"{self.name} equipped a(n) {weapon.name}!")
            if weapon not in self.inventory:
                self.inventory.append(weapon)
            self.weapon = weapon
        else:
            print(f"{weapon} is not a valid weapon.")

    def unequip(self) -> None:
        if self.weapon != self.default_weapon:
            print(f"{self.name} unequipped the {self.weapon.name}!")
            self.inventory.append(self.weapon)
            self.weapon = self.default_weapon
        else:
            print(f"{self.name} has no weapon to unequip!")

    def show_inventory(self) -> None:
        print(f"{self.name}'s Inventory:")
        print('\n'.join(f"- {item.name}" for item in self.inventory))

    def show_item_inventory(self):
        print(f"{self.name}'s Item Inventory:")
        for i, (item, count) in enumerate(self.item_inventory.items(), start=1):
            print(f"{i}. {count}x - {item.name}")


    def use_item(self, item):        
        try:
            self.item_inventory[item] -= 1
        except KeyError:
            print(f"You do not have a {item.name} potion in your inventory.")
        else:
            if item == health_potion:
                self.health = min(self.health + item.effect, self.maxHealth)
                print(f"{self.name} used {item.name} and restored {item.effect} health!")
            elif item == mana_potion:
                self.mana = min(self.mana + item.effect, self.maxMana)
                print(f"{self.name} used {item.name} and restored {item.effect} mana!")
            else:
                print(f"Unknown potion type: {item.name}")

    def sell_weapon(self):
        while True:
            for i, weapon in enumerate(self.inventory, start=1):
                print(f"{i}. {weapon}")
            try:
                if len(self.inventory) > 1:
                    weapon_number = input("Choose a weapon by number or 'q' to quit: ")
                    if weapon_number.lower() == 'q':
                        break
                    weapon_number = int(weapon_number) - 1
                    if 0 <= weapon_number < len(self.inventory):
                        del self.inventory[weapon_number]
                        print("Weapon sold.")
                        break
                    else:
                        print("Invalid weapon number. Please try again.")
                else:
                    print("You can't sell your last weapon.")
                    input("\nPress enter to continue...")
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")
                input("\nPress enter to continue...")

class Enemy(Character):
    def __init__(self, name, health, maxHealth, mana, maxMana, weapon):
        super().__init__(name, health, maxHealth, mana, maxMana)
        self.weapon = weapon
        self.maxHealth = maxHealth
        self.health_bar = HealthBar(self, color="red")

goblin = Enemy(name="Goblin", health=30, maxHealth=30, mana=10, maxMana=100, weapon=short_bow)
ogre = Enemy(name="Ogre", health=50, maxHealth=50, mana=20, maxMana=100, weapon=mace)
troll = Enemy(name="Troll", health=70, maxHealth=70, mana=30, maxMana=100, weapon=iron_sword)
wizard = Enemy(name="Wizard", health=90, maxHealth=90, mana=100, maxMana=100, weapon=magic_staff)
giant = Enemy(name="Giant", health=120, maxHealth=120, mana=50, maxMana=100, weapon=steel_sword)
minotaur = Enemy(name="Minotaur", health=130, maxHealth=130, mana=70, maxMana=100, weapon=battle_axe)
dragon = Enemy(name="Dragon", health=200, maxHealth=200, mana=100, maxMana=100, weapon=fire_breath)