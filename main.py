from abc import ABC, abstractmethod
import random


class Hero(ABC):
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    @abstractmethod
    def attack(self, other):
        pass

    def take_damage(self, damage):
        self.health -= damage
        self.health = max(self.health, 0) 
        print(f"{self.name} получил урон и теперь имеет {self.health} здоровья.")

    def is_alive(self):
        return self.health > 0


class Player(Hero):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=20)

    def attack(self, other):
        damage = self.attack_power
        other.take_damage(damage)
        print(f"{self.name} атакует {other.name} и наносит {damage} урона.")


class Comp(Hero):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=15)

    def attack(self, other):
        damage = self.attack_power
        other.take_damage(damage)
        print(f"{self.name} атакует {other.name} и наносит {damage} урона.")


class Game:
    def __init__(self):
        self.player = Player("Игрок")
        self.computer = Comp("Компьютер")

    def start(self):
        while self.player.is_alive() and self.computer.is_alive():
            if random.random() < 0.5:
                self.player.attack(self.computer)
            else:
                self.computer.attack(self.player)

        winner = self.player.name if self.player.is_alive() else self.computer.name
        print(f"Победитель: {winner}")


game = Game()
game.start()