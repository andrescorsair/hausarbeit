import pygame

pygame.init()

screenWidth = 700
screenHeight = 700

win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Andres Snake Game")

# Attribute für den Charakter(Position muss innerhalb der Fensterauflösung sein). Auflösung = 28x28 (700/25)
x = 50
y = 50
charWidth = 25
charHeight = 25
vel = 10
snakePos = [100, 50]
snakeBody = [[100, 50], [90, 50], [80, 50]]

# Farben
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
neongreen = pygame.Color(0, 255, 70)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

# While Schleife als 'Main Loop'
run = True
while run:
    pygame.time.delay(10) #Clock mit delay in Ms.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel -1:
        x -= vel                          #von der 'x' koordinate subtrahieren für links Bewegung
    if keys[pygame.K_RIGHT]and x < screenWidth - charWidth:
        x += vel
    if keys[pygame.K_UP] and y > vel -1:
        y -= vel
    if keys[pygame.K_DOWN] and y < screenHeight - charHeight:
        y += vel
    if keys [pygame.K_ESCAPE]:
        pygame.event.post(pygame.event.Event(pygame.QUIT))

    win.fill((black))
    char = pygame.draw.rect(win, (neongreen), (x, y, charWidth, charHeight))
    pygame.display.update()

pygame.quit()
