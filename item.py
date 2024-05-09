from dataclasses import dataclass

@dataclass
class Potion:
    name: str
    effect: int
    value: int

    def __init__(self, name: str, effect: int, value: int) -> None:
        self.name = name
        self.effect = effect
        self.value = value
    def __hash__(self) -> int:
        return hash((self.name, self.effect, self.value))
        
    
    # def __eq__(self, other: 'Potion') -> bool:
    #     return self.name == other.name and self.effect == other.effect and self.value == other.value

    # def __eq__(self, other: 'Potion') -> bool:
    #     if isinstance(other, Potion):
    #         return self.name == other.name and self.effect == other.effect and self.value == other.value
    #     elif isinstance(other, str):
    #         return self.name == other

    def __str__(self) -> str:
        return self.name  # Return the name of the potion

health_potion = Potion("Health Potion", 50, 5)
mana_potion = Potion("Mana Potion", 30, 10)