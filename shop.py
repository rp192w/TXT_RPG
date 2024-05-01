from dataclasses import dataclass
from character import Character, Hero
from weapon import Weapon
from item import Potion, health_potion, mana_potion

class Shop:
    def __init__(self):
        self.inventory = [health_potion, mana_potion]

    def sell_weapon(self, hero: 'Hero', weapon: 'Weapon') -> None:
        if len(hero.inventory) > 1:
            try:
                hero.inventory.remove(weapon)
                hero.gold += weapon.value
                print(f"{hero.name} sold {weapon.name} for {weapon.value} gold.")
            except ValueError:
                print("You don't have that weapon in your inventory.")
        else:
            print("You can't sell your last weapon.")

    def buy_potion(self, hero: 'Hero', potion_name: str) -> None:
        potion = next((p for p in self.inventory if p.name == potion_name), None)
        if potion and hero.gold >= potion.value:
            hero.gold -= potion.value
            hero.item_inventory.append(potion)
            print(f"{hero.name} bought {potion.name} for {potion.value} gold.")
        else:
            print("You either don't have enough gold or the potion is not available in the shop.")


class Potion:
    name: str
    effect: int
    value: int

    def use(self, character: 'Character') -> None:
        character.health = min(character.health + self.effect, character.maxHealth)
        character.health_bar.update()
        print(f"{character.name} used {self.name} and restored {self.effect} health!")

    def __str__(self) -> str:
        return self.name  # Return the name of the potion
