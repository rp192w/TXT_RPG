from dataclasses import dataclass

@dataclass
class Potion:
    def __init__(self, name, effect, cost):
        self.name = name
        self.effect = effect
        self.cost = cost

    def use(self, character: 'Character') -> None:
        character.health = min(character.health + self.effect, character.maxHealth)
        character.health_bar.update()
        print(f"{character.name} used {self.name} and restored {self.effect} health!")

    def __str__(self) -> str:
        return self.name  # Return the name of the potion

health_potion = Potion("Health", 50, 5)
mana_potion = Potion("Mana", 10, 10)