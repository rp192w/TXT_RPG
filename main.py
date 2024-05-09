# ------------ Imports ------------
import sys, os, subprocess, item
from character import Hero, Enemy, goblin, ogre, troll, wizard, giant, minotaur, dragon
from weapon import dagger, magic_staff
from story import introLore, goblinIntro, ogreIntro, trollIntro, wizardIntro, giantIntro, minotaurIntro, dragonIntro, dragonOutro, goblinOutro, ogreOutro, trollOutro, wizardOutro, giantOutro, minotaurOutro, dragonOutro, end_game_lore
from shop import Shop
from item import health_potion, mana_potion
from utils import clear_console
# from item import health_potion, mana_potion


# ------------ Enemy Lore ------------
ENEMY_LORE = {
    'Goblin': {'intro': goblinIntro, 'outro': goblinOutro},
    'Ogre': {'intro': ogreIntro, 'outro': ogreOutro},
    'Troll': {'intro': trollIntro, 'outro': trollOutro},
    'Wizard': {'intro': wizardIntro, 'outro': wizardOutro},
    'Giant': {'intro': giantIntro, 'outro': giantOutro},
    'Minotaur': {'intro': minotaurIntro, 'outro': minotaurOutro},
    'Dragon': {'intro': dragonIntro, 'outro': dragonOutro}
}

# ------------ Enemy Lore Function ------------
def enemy_lore(enemy, lore_type):
    lore_func = ENEMY_LORE.get(enemy.name, {}).get(lore_type)
    if lore_func:
        lore = lore_func()
        if lore is not None:
            print(lore)
    else:
        print(f"No {lore_type} lore available for {enemy.name}.")

# ------------ Enemy Intro Lore Function ------------
def enemy_intro_lore(enemy):
    enemy_lore(enemy, 'intro')

# ------------ Enemy Outro Lore Function ------------
def enemy_outro_lore(enemy):
    enemy_lore(enemy, 'outro')
    input("Press Enter to continue...")
    clear_console()
    
# ------------ Reset Game ------------
def reset_game(hero, enemies):
    # Reset the hero
    hero.health = 100  # Replace with the hero's starting health
    hero.mana = 0  # Replace with the hero's starting mana
    hero.inventory = [dagger]  # Replace with the hero's starting inventory

    # Reset the enemies
    for enemy in enemies:
        enemy.health = enemy.maxHealth

# ------------ Start Game Actions ------------
START_GAME_ACTIONS = {
    '1': introLore
}

# ------------ Start Game --------------
def start_game_menu():
    clear_console()
    print("Welcome to the game!")
    print("1. Start Game")
    print("2. End Game")

    choice = input("Choose an option: ")

    if choice == '1':
        hero_name = input("Enter the name for your hero: ")
        hero = Hero(name=hero_name, health=100, maxHealth=100, mana=0, maxMana=100)
        hero.equip(dagger)
        clear_console()
        see_lore = input("Would you like to see the intro lore? (1 for yes, 2 for no): ")
        if see_lore == '1':
            introLore(hero)
        return hero
    elif choice == '2' and dragon.health >= 0:
        print("You could not defeat the dragon. Humanity is doomed for eternity!")
        sys.exit()
    else:
        print("Invalid choice. Please try again.")
        input("Press Enter to continue...")
        return start_game_menu()
    


# ------------ Choose Weapon ------------
def choose_weapon(inventory):
    while True:
        print("Choose a weapon from your inventory:")
        for i, weapon in enumerate(inventory, start=1):
            print(f"{i}. {weapon}")

        weapon_choice = input("Enter the number of the weapon you want to use: ")

        if not weapon_choice.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        weapon_choice = int(weapon_choice) - 1
        if 0 <= weapon_choice < len(inventory):
            return inventory[weapon_choice]
        else:
            print("Invalid choice. Please try again.")


# ------------ Shop Visit ------------
def shop_menu(hero, shop):
    clear_console()
    print("Welcome to the shop!")
    while True:
        print(f"You have {hero.gold} gold.")
        print("1: Sell weapon")
        print("2: Buy health potion")
        print("3: Buy mana potion")
        print("4: Exit shop")

        choice = input("> ")
        if not choice.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        choice = int(choice)
        if choice == 1:  # Sell weapon
            if len(hero.inventory) > 1:  # Cannot sell the last weapon
                sell_weapon(hero, shop)
            else:
                print("You can't sell your last weapon.")
        elif choice in [2, 3]:  # Buy health or mana potion
            item = health_potion if choice == 2 else mana_potion
            shop.buy_item(item, hero)
        elif choice == 4:
            exit_shop(hero)
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def sell_weapon(hero, shop):
    print("Choose a weapon to sell:")
    for i, weapon in enumerate(hero.inventory, start=1):
        print(f"{i}: {weapon.name}")
    weapon_index = input("> ")
    if weapon_index.isdigit() and 0 < int(weapon_index) <= len(hero.inventory):
        shop.sell_weapon(hero, hero.inventory[int(weapon_index) - 1])
    else:
        print("Invalid input. Please choose a valid weapon number.")

def exit_shop(hero):
    print("Exiting shop. Here's your current inventory:")
    print([weapon.name for weapon in hero.inventory], 
        hero.item_inventory[health_potion], "x Health Potions", 
        hero.item_inventory[mana_potion], "x Mana Potions")
    print(f"You have {hero.gold} gold.")
    print("Press Enter to continue...")
    input()

# ------------ Use Item -------------
def battle_use_item(hero):
    if not hero.item_inventory or all(count == 0 for count in hero.item_inventory.values()):
        print("You have no items in your inventory.")
        return

    while True:
        hero.show_item_inventory()
        item_choice = input("Choose an item to use by number or 'q' to quit: ")
        if item_choice.lower() == 'q':
            return

        if not item_choice.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        item_choice = int(item_choice) - 1
        if 0 <= item_choice < len(hero.item_inventory):
            item = list(hero.item_inventory.keys())[item_choice]
            if hero.item_inventory[item] > 0:
                hero.use_item(item)
                break
            else:
                print("You have no more of that item.")
        else:
            print("Invalid item number. Please try again.")


# ------------ Post Victory ------------
def post_victory(hero, enemy):
    if enemy.weapon.name != 'Fists' and 'Fists' not in [weapon.name for weapon in hero.inventory]:
        hero.inventory.append(enemy.weapon)
    hero.item_inventory[health_potion] += 1  # Use the health_potion instance as the key
    if enemy == wizard or wizard.health <= 0:
        hero.item_inventory[mana_potion] += 2
    print_inventory(hero)
    restore_health(hero)
    visit_shop(hero)

def print_inventory(hero):
    print("Hero's inventory after adding enemy weapon and earning potions: ")
    print([weapon.name for weapon in hero.inventory],", ", hero.item_inventory[health_potion],"x Health Potions,", hero.item_inventory[mana_potion],"x Mana Potions")

def restore_health(hero):
    hero.health = hero.maxHealth
    print(f"{hero.name} has been restored to full health!")

def visit_shop(hero):
    shop_choice = input("Do you want to visit the shop? (1 for yes, 2 for no): ")
    if shop_choice == '1':
        shop_menu(hero, shop)

# ------------ Actions Dictionary ------------
ACTIONS = {
    '1': 'attack',
    '2': 'use_item',
    '3': 'mana_attack'
}
# ------------ Battle Menu ------------
def battle_menu():
    while True:
        print("Choose your action:")
        print("1. Attack")
        print("2. Use Item")
        if magic_staff in hero.inventory:
            print("3. Mana Attack")

        choice = input("Enter your choice: ")
        if choice == '':
            return 'attack'

        if choice.isdigit() and 1 <= int(choice) <= 3:
            return ACTIONS.get(choice, None)
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

# ------------ Battle ------------
def battle(hero, enemy):
    while hero.health > 0 and enemy.health > 0:
        clear_console()
        hero.health_bar.draw()
        if magic_staff in hero.inventory:
            hero.mana_bar.draw()
        enemy.health_bar.draw()
        user_choice = battle_menu()  # Get user input in battle_menu function
        if user_choice == 'attack' or user_choice == '':
            hero.attack(enemy)
        elif user_choice == 'mana_attack':
            if hero.mana >= 30 and magic_staff in hero.inventory:
                hero.mana_attack(enemy)
                hero.mana -= 30
            else:
                print("Not enough mana for a mana attack. You lose your turn.")
        elif user_choice == 'use_item':
            battle_use_item(hero)
        else:
            print("Invalid action. You lose your turn.")
        if enemy.health > 0:
            enemy.attack(hero)
        input("Press Enter to continue...")

# -------------- Game Over ----------------
def game_over(hero):
    GAME_OVER_ACTIONS = {
        '1': start_game_menu,
        '2': sys.exit
    }
    print("Game Over!")
    print("Would you like to play again?")
    choice = input("Enter '1' to play again or '2' to quit: ")
    if choice == '1':
        reset_game(hero, enemies)
        return start_game_menu()
    elif choice == '2' and dragon.health <= 0:
        end_game_lore(hero.name)
        sys.exit()
    elif choice == '2':
        print("You could not defeat the dragon. Humanity is doomed for eternity!")
        sys.exit()
    else:
        print("Invalid choice. Please try again.")
        input("Press Enter to continue...")
        return start_game_menu()

# ------------ Main Game Loop ------------
while True:
    hero = start_game_menu()
    clear_console()
    shop = Shop()
    enemies = [goblin, ogre, troll, wizard, giant, minotaur, dragon]

    while True:
        for enemy in enemies:
            clear_console()
            enemy_intro_lore(enemy) # Display the enemy intro lore
            chosen_weapon = choose_weapon(hero.inventory)
            hero.equip(chosen_weapon)
            battle(hero, enemy)
            if hero.health <= 0:
                game_over(hero)
                break
            elif enemy.health <= 0:
                clear_console()
                print(f"{enemy.name} has been defeated!")
                enemy_outro_lore(enemy)
                if enemy == dragon and dragon.health <= 0:
                    print("Congratulations! You have defeated the dragon and saved humanity!")
                    game_over(hero)
                    break  # Break the loop to return to the main menu
                post_victory(hero, enemy)
    input()