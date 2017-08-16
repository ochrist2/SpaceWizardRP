import pygame
display_width = 800
display_height = 600
class character():
    def __init__(self, characterImg, startx, starty):
        self.hp = 4
        self.mana = 100
        self.armour = 50
        self.speed = 10
        self.charx = startx
        self.chary = starty
        self.characterImg = pygame.image.load(characterImg)
        self.forward = False
        self.rightways = False
        self.leftways = True
        self.backwards = False
        self.gravity = -10

    def moveRight(self):
        self.rightways = True
        self.leftways = False

    def moveLeft(self):
        self.rightways = False
        self.leftways = True

    def moveUp(self):
        self.backwards = False
        self.forward = True

    def moveDown(self):
        self.backwards = True
        self.forward = False

    def isAlive(self):
        if self.hp > 0:
            return True
        return False
    def hitLeftWall(self):
        if 0 >= self.charx or self.charx >= display_width:
            return True
        return False