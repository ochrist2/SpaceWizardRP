import random
import pygame

display_width = 800
class projectile:
    def __init__(self, projectileImg, character):
        self.projectileImg = projectileImg
        self.projx = 0 + character.charx
        self.projy = 40 + character.chary
        self.character = character
        self.shotleft = False
        self.shotright = False
        if character.rightways:
            self.projx = 50 + character.charx
            self.projy += -10
        elif character.leftways:
            self.projy += -20
            self.projx += -30

    def move(self, shotleft, shotright):

        i = 0
        if self.character.leftways and not self.shotright:
            self.shotleft = True
        elif self.character.rightways and not self.shotleft:
            self.shotright = True
        if self.shotright:
            i = 1
        elif self.shotleft:
            i = -1
        self.projx += 10*i
        self.projy += 1

    def hasColided(self, astroid):
        if (self.projx + 20 <= astroid.projx + 10 <= self.projx + 80 or self.projx + 20 <= astroid.projx + 35 <= self.projx + 80) and (
                    self.projy <= astroid.projy + 15 <= self.projy + 100 or self.projy <= astroid.projy + 75 <= self.projy + 100):
            astroid.live = False
            return True
        return False


class astroid:
    def __init__(self, projectileImg):
        self.projectileImg = projectileImg
        self.projx = random.randint(0, display_width)
        self.projy = -100
        self.moveleft = False
        self.moveright = False
        self.live = True
        self.timetolive = 30

    def move(self):
        i = 1
        if (random.randint(1, 2) == 1 and not self.moveleft and not self.moveright):
            self.moveleft = True
        elif not self.moveright and not self.moveleft:
            self.moveright = True

        if self.moveleft:
            i = -1
        self.projx += 1 * i
        self.projy += 4

    def hasColided(self, character):
        if (self.projx + 20 <= character.charx + 10 <= self.projx + 80 or self.projx + 20 <= character.charx + 35 <= self.projx + 80) and (self.projy <= character.chary + 15 <= self.projy + 100 or self.projy <= character.chary + 75 <= self.projy + 100):
            character.hp += -1
            character.charx = 400
            character.chary = 400
            return True
        return False
