import os
import time

TEXT_SPEED = 0.02  # Adjust this value to change the speed of the text

def start_game(hero_name):
    lore = [
        f"""
Welcome to the realm of the Ancient Kingdom. You are a brave hero, known as {hero_name}.
        """,
        """
The legend of the ancient dragon has haunted your dreams for as long as you can remember.
        """,
        """ 
The tales tell of a beast of unimaginable size and power, its scales as dark as obsidian, 
and its roar capable of shaking mountains.
        """,
        """ 
The dragon has plagued the land for generations, leaving ruin in its wake and 
terror in the hearts of all who know its name.
        """,
        """
But you are not like the others. You are driven by a deep sense of duty—or perhaps vengeance—to end the dragon's reign and bring peace to the realm. 
        """,
        """   
Your journey will not be easy; you will face countless dangers, from cunning goblins in the forests to sinister wizards in their towers.
        """,
        """
Each step will bring you closer to the final battle, yet every step will also test your courage and resolve.
        """,
        """
The path ahead is shrouded in mystery, but your goal is clear: slay the dragon and restore hope to the world. Gather your strength, equip your weapons, and step into the unknown. Your journey begins now.
        """
    ]
    for text in lore:
        print_with_delay(text, TEXT_SPEED)
        input("\nPress enter to continue...")
        clear_console()

def print_with_delay(text, delay):
    print(''.join(char for char in text), end='', flush=True)
    time.sleep(delay)

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')