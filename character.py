# ------------ imports ------------
from weapon import Weapon, dagger, short_bow, iron_sword, battle_axe, steel_sword, magic_staff, fire_breath, mace
from health_bar import HealthBar, ManaBar
from item import Potion, health_potion, mana_potion

# ------------ parent class setup ------------
class Character:
    def __init__(self,
                 name: str,
                 health: int,
                 maxHealth: int,
                 mana: int,
                 maxMana: int,  
                 gold: int = 0
                 ) -> None:
        self.name = name
        self._health = health
        self.health_bar = HealthBar(self, maxHealth)
        self.mana = mana
        self.mana_bar = ManaBar(self, maxMana)
        self.maxHealth = maxHealth
        self.gold = 0  # Initialize the gold amount


    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = max(0, min(value, self.maxHealth))  # Ensure health is within valid range
#        self.health_bar.draw()  # Redraw the health bar whenever health changes
        
    def attack(self, target) -> None:
        damage = self.weapon.attack()
        target.health -= damage
        print(f"{self.name} dealt {damage} damage to "
              f"{target.name} with {self.weapon.name}")
    def mana_attack(self, target) -> None:
        double_damage = self.weapon.attack() * 3
        target.health -= double_damage

    def __str__(self):
        return self.name


# ------------ Hero Subclass ------------
class Hero(Character):
    def __init__(self, name: str, health: int, maxHealth: int, mana, maxMana) -> None:
        super().__init__(name=name, health=health, maxHealth=maxHealth, mana=mana, maxMana=maxMana)
        self.weapon = dagger
        self.default_weapon = self.weapon
        self.maxHealth = maxHealth
        self.maxMana = maxMana
        self.inventory = [dagger]  # Initialize the inventory with the default weapon
        self.item_inventory = []   # Initialize an empty item inventory
        self.health_bar = HealthBar(self, color="green")  # Initialize the health bar with the color green

    def equip(self, weapon) -> None:
        if isinstance(weapon, Weapon):
            print(f"{self.name} equipped a(n) {weapon.name}!")
            if weapon not in self.inventory:
                self.inventory.append(weapon)  # Add the weapon to the inventory
            self.weapon = weapon
        else:
            print(f"{weapon} is not a valid weapon.")

    def unequip(self) -> None:
        if self.weapon != self.default_weapon:  # Check if the current weapon is not the default weapon
            print(f"{self.name} unequipped the {self.weapon.name}!")
            self.inventory.append(self.weapon)  # Add the current weapon to the inventory
            self.weapon = self.default_weapon  # Equip the default weapon
        else:
            print(f"{self.name} has no weapon to unequip!")

    def show_inventory(self) -> None:
        print(f"{self.name}'s Inventory:")
        print('\n'.join(f"- {item.name}" for item in self.inventory))

    def show_item_inventory(self) -> None:
        print(f"{self.name}'s Item Inventory:")
        print(f"1. {self.item_inventory.count(health_potion)}x - Health Potion (50 HP)")
        print(f"2. {self.item_inventory.count(mana_potion)}x - Mana Potion (10 MP)")
        # for i, item in enumerate(self.item_inventory, start=1):
        #     print(f"{i}. {self.item_inventory.count(item)}x - {item.name} Potion ({item.effect} HP)")

    def use_item(self, item):        
        try:
            self.item_inventory.remove(item)
        except ValueError:
            print(f"You do not have a {item.name} potion in your inventory.")
            return

        if item.name == 'Health':
            self.health = min(self.health + item.effect, self.maxHealth)
            print(f"{self.name} used {item.name} and restored {item.effect} health!")
        elif item.name == 'Mana':
            self.mana = min(self.mana + item.effect, self.maxMana)
            print(f"{self.name} used {item.name} and restored {item.effect} mana!")
        else:
            print(f"Unknown potion type: {item.type}")


# ------------ Enemy Subclass ------------
class Enemy(Character):
    def __init__(self, name, health, maxHealth, mana, maxMana, weapon):
        super().__init__(name, health, maxHealth, mana, maxMana)
        self.weapon = weapon
        self.maxHealth = maxHealth
        self.health_bar = HealthBar(self, color="red")

# ------------ Enemies ------------
goblin = Enemy(name="Goblin", health=30, maxHealth=30, mana=100, maxMana=100, weapon=short_bow)
ogre = Enemy(name="Ogre", health=50, maxHealth=50, mana=100, maxMana=100, weapon=mace)
troll = Enemy(name="Troll", health=70, maxHealth=70, mana=100, maxMana=100, weapon=iron_sword)
wizard = Enemy(name="Wizard", health=90, maxHealth=90, mana=100, maxMana=100, weapon=magic_staff)
giant = Enemy(name="Giant", health=120, maxHealth=120, mana=100, maxMana=100, weapon=steel_sword)
minotaur = Enemy(name="Minotaur", health=130, maxHealth=130, mana=100, maxMana=100, weapon=battle_axe)
dragon = Enemy(name="Dragon", health=200, maxHealth=200, mana=100, maxMana=100, weapon=fire_breath)


