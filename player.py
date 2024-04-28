class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.attack_dmg = 5
        self.hp = 30

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
