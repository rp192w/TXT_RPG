import os
from dataclasses import dataclass
from character import Character, Hero
from weapon import Weapon
from item import Potion, health_potion, mana_potion
from utils import clear_console




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
    def buy_item(self, item, hero):
        if item in self.inventory:
            if hero.gold < item.value:
                print("You don't have enough gold to buy that item.")
                return
            else:
                hero.gold -= item.value
                hero.item_inventory[item] += 1
                print(f"{hero.name} bought {item.name} for {item.value} gold.")
        else:
            print(f"Sorry, we don't have {item.name} in the shop.")
            
    def visit(self, hero: 'Hero') -> None:
        print("Welcome to the shop!")
        print("You have", hero.gold, "gold.")
        print("press enter to continue")
        while True:
            input()
            clear_console()
            print("You have", hero.gold, "gold.")
            print("1: Sell weapon")
            print("2: Buy health potion")
            print("3: Buy mana potion")
            print("4: Exit shop")
            choice = input("> ")
            if choice == '1':
                print("Choose a weapon to sell:")
                for i, weapon in enumerate(hero.inventory, start=1):
                    print(f"{i}: {weapon.name}")
                weapon_index = int(input("> ")) - 1
                self.sell_weapon(hero, hero.inventory[weapon_index])
            elif choice == '2':
                self.buy_potion(hero, 'health_potion')
            elif choice == '3':
                self.buy_potion(hero, 'mana_potion')
            elif choice == '4':
                self.exit_shop()
                return
            else:
                print("Invalid choice. Please choose again.")

    @staticmethod
    def exit_shop():
        print("You have exited the shop.")
        print("press enter to continue")
        input()
