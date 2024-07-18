from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

### Шаг 2: Создание классов Sword и Bow, унаследованных от Weapon

class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."

### Шаг 3: Модификация класса Fighter

class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon

    def attack(self):
        return self.weapon.attack()

### Класс Monster

class Monster:
    def __init__(self, health: int):
        self.health = health

    def is_defeated(self):
        return self.health <= 0

    def take_damage(self, damage: int):
        self.health -= damage

### Шаг 4: Реализация боя

def battle(fighter: Fighter, monster: Monster):
    damage = 10  # простое количество урона за удар
    while not monster.is_defeated():
        print(fighter.attack())
        monster.take_damage(damage)
        if monster.is_defeated():
            print("Монстр побежден!")
        else:
            print(f"У монстра осталось {monster.health} здоровья.")

if __name__ == "__main__":
    sword = Sword()
    bow = Bow()

    fighter = Fighter(sword)
    monster = Monster(health=30)

    # Боец сначала использует меч
    print("Боец выбирает меч.")
    battle(fighter, monster)

    # Создаем нового монстра для следующего боя
    monster = Monster(health=30)

    # Боец меняет оружие на лук
    fighter.changeWeapon(bow)
    print("\nБоец выбирает лук.")
    battle(fighter, monster)
