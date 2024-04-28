class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 10
        self.attack_dmg = 3

    def move(self, player_x, player_y):
        if self.x < player_x:
            self.x += 1
        elif self.x > player_x:
            self.x -= 1
        if self.y < player_y:
            self.y += 1
        elif self.y > player_y:
            self.y -= 1

