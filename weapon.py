from random import randrange
from dataclasses import dataclass

@dataclass
class Weapon:
    name: str
    weapon_type: str
    min_damage: int
    max_damage: int
    value: int

    def attack(self) -> int:
        return randrange(self.min_damage, self.max_damage + 1)

    def __str__(self) -> str:
        return self.name

# ------------ Weapons ------------
dagger = Weapon(name="Dagger", weapon_type="sharp", min_damage=1, max_damage=3, value=5)
short_bow = Weapon(name="Short Bow", weapon_type="ranged", min_damage=1, max_damage=4, value=10)
mace = Weapon(name="Mace", weapon_type="ranged", min_damage=1, max_damage=5, value=15)
iron_sword = Weapon(name="Iron Sword", weapon_type="sharp", min_damage=1, max_damage=6, value=20)
magic_staff = Weapon(name="Magic Staff", weapon_type="magic", min_damage=1, max_damage=7, value=50)
long_bow = Weapon(name="Long Bow", weapon_type="ranged", min_damage=2, max_damage=8, value=60)
battle_axe = Weapon(name="Battle Axe", weapon_type="sharp", min_damage=2, max_damage=9, value=80)
steel_sword = Weapon(name="Steel Sword", weapon_type="sharp", min_damage=3, max_damage=12, value=100)
fire_breath = Weapon(name="Fire Breath", weapon_type="elemental", min_damage=5, max_damage=15, value=100)