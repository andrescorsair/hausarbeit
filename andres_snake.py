import pygame
from random import randint

pygame.init()

#Variablen für Gamewindow
screenWidth = 700
screenHeight = 700

win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Andres Snake Game")

# Attribute für den Charakter(Position muss innerhalb der Fensterauflösung sein). Auflösung = 28x28 (700/25)
size = 25
snakeBody = [[3, 1], [2, 1], [1, 1]] #startlänge
snakePos = [3, 1]                    #Kopf der Schlange
direction = 'RIGHT'                  #Startrichtung
changedir = ''
applePos = [6, 6]
Punkte = 0

# Farben (RGB)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
neongreen = pygame.Color(0, 255, 70)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)


# Gitter für Gamewindow
def grid(num):
    return num * size


# While Schleife als 'Main Loop'
run = True
while run:  #
    #  print(snakeBody)
    pygame.time.delay(100)  # Clock mit delay in Ms.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # collision apple
    def apple_collision(head, apple):
        if head == apple:
            return True
        else:
            return False

    # collision snake
    def self_collision(body):
        for i in body:
            if body.count(i) > 1:
                return True
            else:
                return False

    # collision window
    def window_collision(head, grid_size):
        if head[0] < 0 or head[0] > grid_size or head[1] < 0 or head[1] > grid_size:
            return True
        else:
            return False


    # place apple in free spot
    def place_apple(blocked):
        pos = []
        i = 0
        while i < size ** 2:
            pos = (randint(0, screenWidth/size-1), randint(0, screenHeight/size-1))
            for element in blocked:
                if pos == element:
                    continue
            return pos


        applePos[0] = randint(0, screenWidth / size - 1)
        applePos[1] = randint(0, screenHeight / size - 1)

    # Definition Keyboard Tasten
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        direction = 'LEFT'
    if keys[pygame.K_RIGHT]:
        direction = 'RIGHT'
    if keys[pygame.K_UP]:
        direction = 'UP'
    if keys[pygame.K_DOWN]:
        direction = 'DOWN'
    if keys[pygame.K_ESCAPE]:
        pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Update snake position
    if direction == 'RIGHT':
        snakePos[0] += 1
    if direction == 'LEFT':
        snakePos[0] -= 1
    if direction == 'DOWN':
        snakePos[1] += 1
    if direction == 'UP':
        snakePos[1] -= 1

    if not apple_collision(snakePos, applePos):
        snakeBody.pop()
    else:
        applePos[0] = randint(0, screenWidth/size-1)
        applePos[1] = randint(0, screenHeight/size-1)
    snakeBody.insert(0, list(snakePos))

    # hintergrund draw black
    win.fill(black)

    # draw apple
    pygame.draw.rect(win, red, (grid(applePos[0])+2, grid(applePos[1])+2, size-4, size-4))

    # draw snake
    for element in snakeBody:
        pygame.draw.rect(win, neongreen, (grid(element[0])+2, grid(element[1])+2, size-4, size-4))

    if self_collision(snakeBody):
        pygame.QUIT()
        print('self crash')
    if window_collision(snakePos, screenWidth/size):
        pygame.QUIT()
        print('window crash')
    pygame.display.update()

pygame.quit()
