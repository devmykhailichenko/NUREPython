class Character:
    def __init__(self, name, health, energy):
        self.name = name
        self.__health = health
        self._energy = energy

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, new_health):
        if new_health < 0:
            self.__health = 0
        else:
            self.__health = new_health

    @property
    def energy(self):
        return self._energy

    @energy.setter
    def energy(self, new_energy):
        if new_energy < 0:
            self._energy = 0
        else:
            self._energy = new_energy

    def is_alive(self):
        return self.__health > 0

    def attack(self, target):
        print(f"{self.name} is attacking {target.name}")

    def show_status(self):
        print(f"{self.name}: health={self.health}, energy={self.energy}")

    def __str__(self):
        print(f"{self.name}: health={self.health}, energy={self.energy}")


class Warrior(Character):
    def __init__(self, name, health, energy, armor):
        super().__init__(name, health, energy)
        self.armor = armor

    def attak(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attak! He/she/they is dead...")

        if not target.is_alive():
            print(f"{target.name} is defeated...")

        if self.energy < 10:
            print(f"{self.name} has not enough energy")

        self.energy -= 10

        target.health -= 15 - self.armor_block(target)

    def armor_block(self, target):
        if isinstance(target, Warrior):
            return target.armor
        return 0

    def defend(self):
        self.armor += 2
        print(f"{self.name} increase armor by 2")


if __name__ == "__main__":
    print("Main")