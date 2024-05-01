import math

class Bar:
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
        raise NotImplementedError("This method should be overridden in a subclass")

    def draw(self) -> None:
            bar = self.symbol_remaining * math.ceil(self.current_value)
            bar = bar.ljust(self.length, self.symbol_lost)
            bar = self.colorize(bar) if self.is_colored else bar
            print(f"{self.entity.name}'s {self.bar_name}: {self.current_value}/{self.max_value}")
            print(f"{self.barrier}{bar}{self.barrier}")


    def colorize(self, text):
        return f"{self.color}{text}{self.colors['default']}"
    
    def update(self):
        return self.entity.health

class HealthBar(Bar):
    bar_name = "HEALTH"
    
    @property
    def current_value(self):
        return self.entity.health

    @property
    def max_value(self):
        return self.entity.maxHealth

    def __init__(self, entity, length: int = 20, is_colored: bool = True, color: str = "green") -> None:
        super().__init__(entity, length, is_colored, color)

class ManaBar(Bar):
    bar_name = "MANA"

    @property
    def current_value(self):
        return self.entity.mana

    @property
    def max_value(self):
        return self.entity.maxMana
    
    def __init__(self, entity, length: int = 20, is_colored: bool = True, color: str = "blue") -> None:
        super().__init__(entity, length, is_colored, color)

