import pygame
import char
import projectile
pygame.init()
display_width = 800
display_height = 600
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Space Wizard Ryan Pike')
clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def display_score(text, x, y):
    largeText = pygame.font.Font('freesansbold.ttf', 30)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    #time.sleep(2)


def show(x, y, img):
    gameDisplay.blit(img, (x, y))


def game_loop():
    quitted = False
    character = char.character('art/wizard.png', 400, 400)
    astroids = []
    charx_changed = 0
    shots = []
    astroidcounter = 0
    playagain = False
    score = 0
    showScores = False
    while not quitted and (character.isAlive() or not playagain):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitted = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    charx_changed = -15
                    character.characterImg = pygame.image.load('art/wizard.png')
                    character.moveLeft()
                if event.key == pygame.K_d:
                    character.characterImg = pygame.image.load('art/wizard_right.png')
                    character.moveRight()
                    charx_changed = 15
                if event.key == pygame.K_SPACE:
                    character.chary += -60
                if event.key == pygame.K_p:
                    if character.leftways:
                     shots.append(projectile.projectile(pygame.image.load('art/fireballL.png'), character))
                    elif character.rightways:
                        shots.append(projectile.projectile(pygame.image.load('art/fireball.png'), character))
                if event.key == pygame.K_RETURN:
                    playagain = True
                if event.key == pygame.K_TAB:
                    showScores = not showScores
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    charx_changed = 0
        for x in shots:
            if 0 <= x.projx <= display_width - 50 and 0 <= x.projy <= display_height - 50:
                x.move(x.shotleft, x.shotright)
            else:
                shots.remove(x)
        if character.isAlive():
            score += 5
            character.charx += charx_changed
            if character.chary + 100 <= display_height:
                character.chary += -character.gravity
        show(0, 0, pygame.image.load('art/bg.png'))
        show(character.charx, character.chary, character.characterImg)
        astroidcounter += 1
        if astroidcounter == 5:
            astroids.append(projectile.astroid(pygame.image.load('art/astroid.png')))
            astroidcounter = 0
        for x in astroids:
            x.move()
            show(x.projx, x.projy, x.projectileImg)
            if x.hasColided(character):
                astroids.clear()
                shots.clear()
        if not character.isAlive():
            if showScores:
                scores = []
                try:
                    file = open('scores', 'r')
                    for x in file:
                        scores.append(int(x.strip('\n')))
                except FileNotFoundError:
                    print('no scores')
                scores.sort(reverse=True)
                show(0, 0, pygame.image.load('art/background.jpg'))
                count = 0
                for x in scores:
                    display_score(str(x), (display_width/2), 100 * (count+1) - 75)
                    count += 1

            else:
                character.characterImg = pygame.image.load('art/begone.png')
                #show(220, 0, pygame.image.load('art/playagain.png'))
                character.charx = -100
                character.chary = -100
                display_score('Press Enter to play again', (display_width / 2),
                              display_height - 200)
                display_score('your score: ' + str(score) + ' || press tab for highscores', (display_width/2), display_height - 100)

            if playagain:
                astroids.clear()
                character.characterImg = pygame.image.load('art/wizard.png')
                character.hp = 3
                character.charx = 400
                character.chary = 400
                file = open('scores', 'a')
                score = str(score) + '\n'
                file.write(score)
                file.close()
                score = 0
        else:
            for x in shots:
                show(x.projx, x.projy, x.projectileImg)
                for i in astroids:
                    if x.hasColided(i):
                        show(i.projx, i.projy, pygame.image.load('art/explosion.png'))
                        try:
                            astroids.remove(i)
                            shots.remove(x)
                        except ValueError:
                            print('whoops')

            for i in range(character.hp):
                show(display_width - 300 + (50 * i), 100, pygame.image.load('art/heart.png'))

            display_score('Score: ' + str(score), 200, 100)
        pygame.display.update()
        clock.tick(60)
        playagain = False
game_loop()
pygame.quit()
quit()
