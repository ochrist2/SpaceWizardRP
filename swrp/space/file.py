import pygame
pygame.init()#
display_width = 800
display_height = 600
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
ship_width = 200
ship_height = 200
gameDisplay = pygame.display.set_mode((display_width, display_height))#has to be a touple
pygame.display.set_caption('Space')
clock = pygame.time.Clock()

def shoot(forward, backwards, rightways, leftways, bulletImg, shipx, shipy):
    for i in range(3):
        if forward:
            bulletx = shipx + 80
            bullety = shipy - (50 * i) - 50
            show(shipx + 80, shipy - (50 * i) - 50, bulletImg[0])
        if backwards:
            bulletx = shipx + 80
            bullety = shipy + (50 * i) + 200
            show(shipx + 80, shipy + (50 * i) + 200, bulletImg[0])
        if leftways:
            bulletx = shipx - (50 * i) - 30
            bullety = shipy + 80
            show(shipx - (50 * i) - 30, shipy + 80, bulletImg[0])
        if rightways:
            bulletx = shipx + (50 * i) + 200
            bullety = shipy + 80
            show(shipx + (50 * i) + 200, shipy + 80, bulletImg[0])
    return (bulletx, bullety)
def show(x, y, img):
    gameDisplay.blit(img, (x, y))
def hitMoon(objx, objy):
    if 0 <= objx <= 300 and 0 <= objy <= 300:
        return True
    return False
def game_loop():
    spaceshipImg = pygame.image.load('spaceship.png')
    moonImg = pygame.image.load('moon.png')
    gameOverImg = pygame.image.load('game_over.png')
    heartImg = [pygame.image.load('heart.png'), pygame.image.load('heart.png'), pygame.image.load('heart.png')]
    bulletImg = [pygame.image.load('bullet.png'), pygame.image.load('bullet.png'), pygame.image.load('bullet.png')]
    count = 0
    shipx = display_width * 0.45
    shipy = display_height * 0.6
    moonx = 100
    moony = 100
    x_changed = 0
    y_change = 0
    crashed = False
    quitted = False
    lifes = 3
    alive = True
    shot = False
    forward = True
    backwards = False
    rightways = False
    leftways = False
    bulletx = display_width
    bullety = display_height
    while not quitted and alive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitted = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    rightways = False
                    leftways = True
                    x_changed = -5
                    spaceshipImg = pygame.image.load('spaceship_left.png')
                elif event.key == pygame.K_RIGHT:
                    x_changed = 5
                    rightways = True
                    leftways = False
                    spaceshipImg = pygame.image.load('spaceship_right.png')
                elif event.key == pygame.K_UP:
                    y_change = -5
                    forward = True
                    backwards = False
                    spaceshipImg = pygame.image.load('spaceship.png')
                elif event.key == pygame.K_DOWN:
                    y_change = 5
                    forward = False
                    backwards = True
                    spaceshipImg = pygame.image.load('spaceship_down.png')
                elif event.key == pygame.K_SPACE:
                    shot = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_changed = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                elif event.key == pygame.K_SPACE:
                    shot = False

        shipx += x_changed
        shipy += y_change
        # draw things
        gameDisplay.fill(white)
        show(shipx, shipy, spaceshipImg)
        if shot:
            bulletxy = shoot(forward, backwards, rightways, leftways, bulletImg, shipx, shipy)
            bulletx = bulletxy[0]
            bullety = bulletxy[1]
            print(str(bulletx) + '\t' + str(bullety) + '\t' + str(moonx) + '\t' + str(moony))
        # print(str(shipx) + "\t" + str(shipy))
        # this to ##########################################
        if hitMoon(bulletx, bullety):#########
            moonx = 0                               ########
            moony = 0                               ########
            moonImg = pygame.image.load('bebang.png')#######
            count += 1                              ########
        if count > 30:                              ########
            moonImg  = pygame.image.load('begone.png')######
        # this handles the moon exploding###################

        # update the screen
        if shipx > display_width - ship_width or shipx < 0 or shipy > display_height - ship_height or shipy < 0:
            crashed = True
        if crashed:
            shipx = display_width * 0.45
            shipy = display_height * 0.6
            lifes = lifes - 1
            crashed = False
        if lifes == 0:
            alive = False
            show(0, 0, gameOverImg)
            moonImg = pygame.image.load('begone.png')
        for i in range(lifes):
            show(display_width - 300 + (50 * i), 100, heartImg[i])
        show(moonx, moony, moonImg)
        pygame.display.update()
        clock.tick(30)
game_loop()
pygame.quit()
quit()
