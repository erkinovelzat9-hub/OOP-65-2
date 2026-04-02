# class Hero:
#
#     # Контруктором класса
#     def __init__(self, name, hp, lvl):
#         # Атрибуты класса
#         self.name_hero = name
#         self.hp_hero = hp
#         self.lvl_hero = lvl
#
#
#
# kirito = Hero(name="Кирито", hp=1000, lvl=1000)
#
# print(kirito.name)
#

class Hero:
    def __init__(self, name, hp, lvl):
        self.name = name
        self.hp = hp
        self.lvl = lvl


kirito = Hero(name="Кирито", hp=1000, lvl=1000)


print(kirito.name)