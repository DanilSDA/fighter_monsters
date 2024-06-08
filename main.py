# Задание: Применение Принципа Открытости/Закрытости (Open/Closed Principle) в Разработке Простой Игры
#
# Цель: Цель этого домашнего задание - закрепить понимание и навыки применения принципа открытости/закрытости (Open/Closed Principle), одного из пяти SOLID принципов объектно-ориентированного программирования. Принцип гласит, что программные сущности (классы, модули, функции и т.д.) должны быть открыты для расширения, но закрыты для модификации.
#
# Задача: Разработать простую игру, где игрок может использовать различные типы оружия для борьбы с монстрами. Программа должна быть спроектирована таким образом, чтобы легко можно было добавлять новые типы оружия, не изменяя существующий код бойцов или механизм боя.
#
# Исходные данные:
#
# Есть класс Fighter, представляющий бойца.
# Есть класс Monster, представляющий монстра.
# Игрок управляет бойцом и может выбирать для него одно из вооружений для боя.
# Шаг 1: Создайте абстрактный класс для оружия
#
# Создайте абстрактный класс Weapon, который будет содержать абстрактный метод attack().
# Шаг 2: Реализуйте конкретные типы оружия
#
# Создайте несколько классов, унаследованных от Weapon, например, Sword и Bow. Каждый из этих классов реализует метод attack() своим уникальным способом.
# Шаг 3: Модифицируйте класс Fighter
#
# Добавьте в класс Fighter поле, которое будет хранить объект класса Weapon.
# Добавьте метод changeWeapon(), который позволяет изменить оружие бойца.
# Шаг 4: Реализация боя
#
# Реализуйте простой механизм для демонстрации боя между бойцом и монстром, исходя из выбранного оружия.
# Требования к заданию:
#
# Код должен быть написан на Python.
# Программа должна демонстрировать применение принципа открытости/закрытости: новые типы оружия можно легко добавлять, не изменяя существующие классы бойцов и механизм боя.
# Программа должна выводить результат боя в консоль.
# Пример результата:
#
# Боец выбирает меч

# Боец наносит удар мечом.
#
# Монстр побежден!
#
# Боец выбирает лук.
#
# Боец наносит удар из лука.
#
# Монстр побежден!

from abc import ABC,abstractmethod
class Weapon(ABC):
    def __init__(self,name, damage):
        self.name = name
        self.damage = damage
    @abstractmethod
    def attack(self):
        pass

    def getname(self):
        return self.name



class Bow(Weapon):
    def attack(self):
        print(f"выстрел из {self.name}")

class Sword(Weapon):
    def attack(self):
        print(f"удар с использованием {self.name}")


class Monster():
    def __init__(self,name, health):
        self.name = name
        self.health = health
    def harm(self,harm:int):
        if harm > 0:
            self.health =  self.health - harm
            if self.health<=0:
                print(f'Монстер {self.name} убит')
            else:
                print(f'Монстер {self.name} получил ущерб ')



class Fighter():
    def __init__(self,name, health):
        self.name = name
        self.health = health

    def choose_weapon(self,new_weapon:Weapon):
        self.armor = new_weapon
        print(f"Боец {self.name} выбрал {self.armor.getname()}")

    def attack_with_weapon(self):
        self.armor.attack()

    def harm_monster(self, monster: Monster):

        monster.harm(self.armor.damage)

bow_asg = Bow("Асгард Лук", 300)
sword_artur = Sword("Меч Артура", 500)
figher_heracl = Fighter("Геракл", 5500)
monster_hidra = Monster("Гидра",800)

figher_heracl.choose_weapon(sword_artur)
figher_heracl.attack_with_weapon()
figher_heracl.harm_monster(monster_hidra)
figher_heracl.choose_weapon(bow_asg)
figher_heracl.attack_with_weapon()
figher_heracl.harm_monster(monster_hidra)
