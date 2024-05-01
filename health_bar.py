import math

class HealthBar:
    symbol_remaining: str = "█"
    symbol_lost: str = "_"
    barrier: str = "|"
    colors: dict = {
        "red": "\033[91m",
        "purple": "\33[95m",
        "blue": "\33[34m",
        "blue2": "\33[36m",
        "blue3": "\33[96m",
        "green": "\033[92m",
        "green2": "\033[32m",
        "brown": "\33[33m",
        "yellow": "\33[93m",
        "grey": "\33[37m",
        "default": "\033[0m"
    }

    def __init__(self, entity, length: int = 20, is_colored: bool = True, color: str = "") -> None:
        self.entity = entity
        self.length = length
        self.is_colored = is_colored
        self.color = self.colors.get(color) or self.colors["default"]

    @property
    def current_value(self):
        return self.entity.health


    def draw(self) -> None:
        health_bar = self.symbol_remaining * math.ceil(self.current_value)
        health_bar = health_bar.ljust(self.length, self.symbol_lost)
        health_bar = self.colorize(health_bar) if self.is_colored else health_bar
        print(f"{self.entity.name}'s HEALTH: {self.current_value}/{self.entity.maxHealth}")
        print(f"{self.barrier}{health_bar}{self.barrier}")

    def colorize(self, text):
        return f"{self.color}{text}{self.colors['default']}"
    
    def update(self):
        return self.entity.health

class ManaBar:
    def __init__(self, character, max_mana):
        self.character = character
        self.max_mana = max_mana

    def draw(self):
        mana_bar = self.symbol_remaining * self.character.mana
        mana_bar = mana_bar.ljust(self.length, self.symbol_lost)
        mana_bar = self.colorize(mana_bar) if self.is_colored else mana_bar
        print(f"{self.character.name}'s MANA: {self.character.mana}/{self.max_mana}")
        print(f"{self.barrier}{mana_bar}{self.barrier}")