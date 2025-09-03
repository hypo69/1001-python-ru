import random

class Tank:
    """
    Базовый класс для танков.
    """
    def __init__(self, model: str, armor: int, min_damage: int, max_damage: int, health: int) -> None:
        """
        Инициализация танка.
         
        Args:
            model: Модель танка.
            armor: Броня танка.
            min_damage: Минимальный урон танка.
            max_damage: Максимальный урон танка.
            health: Здоровье танка.
        """
        self.model = model
        self.armor = armor
        self.min_damage = min_damage  # Сохраняем минимальный урон
        self.max_damage = max_damage  # Сохраняем максимальный урон
        self.health = health
        
    def calculate_damage(self) -> int:
        """
        Вычисляет случайный урон танка в заданном диапазоне.

        Returns:
             Случайный урон.
        """
        return random.randint(self.min_damage, self.max_damage)

    def print_info(self) -> None:
        """
        Выводит информацию о танке.
        """
        print(f"{self.model} имеет лобовую броню {self.armor}мм при {self.health}ед. здоровья и урон в диапазоне от {self.min_damage} до {self.max_damage} единиц")

    def health_down(self, enemy_damage: int) -> None:
        """
        Уменьшает здоровье танка.
        
        Args:
             enemy_damage: Урон, нанесенный противником.
        """
        self.health -= enemy_damage
        print(f"\n{self.model}:")
        print(f"Командир, по экипажу {self.model} попали, у нас осталось {self.health} очков здоровья")

    def shot(self, enemy: object) -> None:
        """
        Танк стреляет по противнику.
        
        Args:
            enemy: Танк-противник.
        """
        damage = self.calculate_damage() # Вычисляем урон
        if enemy.health <= 0 :
             print(f"Экипаж танка {enemy.model} уже уничтожен")
        elif damage >= enemy.health:
            enemy.health = 0
            print(f"\n{self.model}:")
            print(f"Экипаж танка {enemy.model} уничтожен")
        else:
            enemy.health_down(damage)
            print(f"\n{self.model}:")
            print(f"Точно в цель, у противника {enemy.model} осталось {enemy.health} единиц здоровья")


class SuperTank(Tank):
    """
    Класс для супертанка, наследуется от Tank.
    """
    def __init__(self, model: str, armor: int, min_damage: int, max_damage: int, health: int) -> None:
        """
        Инициализация супертанка.
        
        Args:
            model: Модель танка.
            armor: Броня танка.
            min_damage: Минимальный урон танка.
            max_damage: Максимальный урон танка.
            health: Здоровье танка.
        """
        super().__init__(model, armor, min_damage, max_damage, health)
        self.forceArmor = True

    def health_down(self, enemy_damage: int) -> None:
        """
        Уменьшает здоровье супертанка с учетом повышенной брони.
        
        Args:
            enemy_damage: Урон, нанесенный противником.
        """
        effective_damage = max(0, enemy_damage - self.armor // 2) # Уменьшаем урон в зависимости от брони
        self.health -= effective_damage
        print(f"\n{self.model}:")
        print(f"Командир, по экипажу {self.model} попали, у нас осталось {self.health} очков здоровья")

def main():
    """
    Основная функция игры.
    """
    tank1 = Tank("Т-34", 50, 20, 30, 100)
    tank2 = SuperTank("Тигр", 80, 25, 35, 150)

    print("Начинается танковый бой!")
    tank1.print_info()
    tank2.print_info()

    current_tank = tank1
    enemy_tank = tank2

    while tank1.health > 0 and tank2.health > 0:
        current_tank.shot(enemy_tank)
        current_tank, enemy_tank = enemy_tank, current_tank  # Смена очереди

    if tank1.health <= 0:
        print(f"\nПобедил {tank2.model}!")
    else:
        print(f"\nПобедил {tank1.model}!")

if __name__ == "__main__":
    main()