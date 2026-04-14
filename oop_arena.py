import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.potions = 3

    def attack(self):
        return random.randint(15, 30)

    def take_damage(self, damage):
        self.hp -= damage
        return f"{self.name} took {damage} damage! (HP left: {self.hp})"

    def heal(self):
        if self.potions > 0:
            self.hp += 30
            if self.hp > 100:
                self.hp = 100
            self.potions -= 1
            return f"🧪 {self.name} used a potion! HP is now {self.hp}."
        else:
            return "❌ You reach into your bag, but you are out of potions! 💀"


class Monster:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self):
        return random.randint(10, 40)

    def take_damage(self, damage):
        self.hp -= damage
        return f"🔥 {self.name} took {damage} damage! (HP left: {self.hp})"