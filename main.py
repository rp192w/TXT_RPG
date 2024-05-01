# ------------ Imports ------------
import sys, os
from character import Hero, Enemy, goblin, ogre, troll, wizard, giant, minotaur, dragon
from weapon import dagger, short_bow, iron_sword, battle_axe, steel_sword, magic_staff, fire_breath
from story import start_game, goblinIntro, ogreIntro, trollIntro, wizardIntro, giantIntro, minotaurIntro, dragonIntro, dragonOutro, goblinOutro, ogreOutro, trollOutro, wizardOutro, giantOutro, minotaurOutro, dragonOutro, end_game
from shop import Shop
from item import health_potion, mana_potion


# ------------ Choose Weapon ------------
def choose_weapon(inventory):
    print("Choose a weapon from your inventory:")
    for i, weapon in enumerate(inventory, start=1):
        print(f"{i}. {weapon}")

    while True:
        try:
            weapon_choice = int(input("Enter the number of the weapon you want to use: ")) - 1
            if 0 <= weapon_choice < len(inventory):
                return inventory[weapon_choice]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

#------------ Shop Visit ------------
def shop_visit(hero, shop):
    while True:
        clear_console()
        print("Welcome to the shop! What would you like to do?")
        print("Your gold: ", hero.gold)
        print("1. Sell a weapon")
        print("2. Buy a potion")
        print("3. Exit the shop")
        choice = input("> ")
        if choice == '1':
            for i, weapon in enumerate(hero.inventory, start=1):
                print(f"{i}. {weapon}")
            while True:
                try:
                    if len(hero.inventory) > 1:
                        weapon_number = int(input("Choose a weapon by number: ")) - 1
                        if 0 <= weapon_number < len(hero.inventory):
                            weapon = hero.inventory[weapon_number]
                            hero.inventory.remove(weapon)
                            hero.gold += weapon.value
                            print(f"You sold {weapon.name} for {weapon.value} gold. You now have {hero.gold} gold.")
                            break
                        else:
                            print("Invalid weapon number. Please try again.")
                    else:
                        print("You can't sell your last weapon.")
                        input("\nPress enter to continue...")
                        break
                except ValueError:
                    print("Invalid input. Please enter a number.")
        elif choice == '2':
            shop.buy_potion(hero, "Health")
        elif choice == '3':
            print("Hero's inventory after your shop visit: ", [weapon.name for weapon in hero.inventory], hero.item_inventory.count(health_potion),"x Health Potions")
            break

# ------------ Use Item -------------

def battle_use_item(hero):
    if not hero.item_inventory:
        print("You have no items in your inventory.")
        return
    else:
        hero.show_item_inventory()
        while True:
            try:
                item_number = int(input("Choose an item by number: ")) - 1
                if 0 <= item_number < len(hero.item_inventory):
                    try:
                        item = hero.item_inventory[item_number]
                        hero.use_item(item)
                    except ValueError:
                        print(f"You do not have a {item.name} potion in your inventory.")
                        return
                    
                    break
                else:
                    print("Invalid item number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")


# ------------ Post Victory ------------
def post_victory(hero, enemy):
    if enemy.weapon.name != 'Fists' or 'Fists' not in [weapon.name for weapon in hero.inventory]:
        hero.inventory.append(enemy.weapon)
    hero.item_inventory.append(health_potion)
    hero.item_inventory.append(mana_potion)
    
    print("Hero's inventory after adding enemy weapon and earning a potion: ", [weapon.name for weapon in hero.inventory], hero.item_inventory.count(health_potion),"x Health Potions")
    # item_choice = input("Would you like to use the item you just earned? (yes/no): ")
    # if item_choice.lower() == 'yes':
    #     hero.use_item(health_potion)
    shop_choice = input("Would you like to visit the shop? (yes/no): ")
    if shop_choice .lower() == 'yes':
        shop_visit(hero, shop)

# ----------- Rest Question ------------
def rest_question():
    rest = input("Would you like to rest before fighting again? (yes/no): ")
    if rest.lower() == 'yes':
        hero.health = original_hero_health
        print(f"{hero.name} has been restored to full health!")

# ------------ Start Game --------------
def start_game_page():
    clear_console()
    print("Welcome to the Text RPG!")
    print("1. Start new game")
    print("2. Exit game")
    choice = input("> ")
    if choice == '1':
        hero_name = input("Enter the name for your hero: ")
        hero_health = 100
        hero_mana = 0
        hero_maxHealth = 100
        hero_maxMana = 100
        hero = Hero(name=hero_name, health=hero_health, maxHealth=hero_maxHealth, mana=0, maxMana=100)
        hero.equip(dagger)
        clear_console()
        see_lore = input("Would you like to see the intro lore? (yes/no): ")
        if see_lore.lower() == 'yes':
            start_game(hero_name)
        return hero
    elif choice == '2':
        sys.exit()
    else:
        print("Invalid choice. Please try again.")
        return start_game_page()
    
# ------------ Enemy Intro Lore ----------------
def enemy_intro_lore(enemy):
    if enemy == goblin:
        goblinIntro()
    elif enemy == ogre:
        ogreIntro()
    elif enemy == troll:
        trollIntro()
    elif enemy == wizard:
        wizardIntro()
    elif enemy == giant:
        giantIntro()
    elif enemy == minotaur:
        minotaurIntro()
    elif enemy == dragon:
        dragonIntro()
    
# ------------ Clear Screen --------------
def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == "__main__":
    hero = start_game_page()
    clear_console()
    shop = Shop()
    original_hero_health = hero.health

    enemies = [goblin, ogre, troll, wizard, giant, minotaur, dragon]

    while True:
        for enemy in enemies:
            clear_console()
            enemy_intro_lore(enemy) # Display the enemy intro lore
            chosen_weapon = choose_weapon(hero.inventory)
            hero.equip(chosen_weapon)
            while hero.health > 0 and enemy.health > 0:
                hero.health_bar.draw()
                hero.mana_bar.draw()
                enemy.health_bar.draw()
                print("Do you want to (1) Attack, (2) Mana Attack, or (3) Use an item?")
                action = input("> ")
                if action == '1' or action == '':
                    hero.attack(enemy)
                elif action == '2':
                    hero.mana_attack(enemy)
                elif action == '3':
                    battle_use_item(hero)
                else:
                    print("Invalid action. You lose your turn.")
                if enemy.health > 0:
                    enemy.attack(hero)
                input("Press Enter to continue...")
                clear_console()
            if hero.health <= 0:
                print(f"{hero.name} has been defeated. Game Over.")
                sys.exit()
            elif enemy.health <= 0:
                if enemy == dragon and dragon.health <= 0:
                    print("Congratulations! You have defeated the dragon!")
                    break  # Break the loop to return to the main menu
                post_victory(hero, enemy)
                rest_question()
    input()