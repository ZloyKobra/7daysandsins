# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

init python:
    class MyCharacter:
        def __init__(self, name, hp, mind, healing_items, mind_items, damaging_items):
            self.name = name
            self.hp = hp
            self.mind = mind
            self.healing_items = healing_items
            self.mind_items = mind_items
            self.damaging_items = damaging_items

        def perform_attack(self, target, damage):
            target.hp -= damage
            if target.hp < 0:
                target.hp = 0
        def perform_mind_attack(self, target, damage):
            target.mind -= damage
            if target.mind < 0:
                target.mind = 0

# Игра начинается здесь:
label start:
    
    $ gg_name = renpy.input("Назовите главного героя")

    jump intro

    return
