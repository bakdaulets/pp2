import pygame
pygame.init()
SIZE = WIDTH, HIGHT = 700, 700
WHITE = (255, 255, 255)
RED = (253, 16, 59)
FPS = 60
RADIUS = 25
x = WIDTH // 2
y = HIGHT // 2
speed = 10
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x - RADIUS - speed >= 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x + RADIUS + speed <= WIDTH:
        x += speed
    if keys[pygame.K_UP] and y - RADIUS - speed >= 0:
        y -= speed
    if keys[pygame.K_DOWN] and y + RADIUS + speed <= HIGHT:
        y += speed
    screen.fill(WHITE)
    circle = pygame.draw.circle(screen, RED, (x, y), RADIUS)
    pygame.display.update()
    clock.tick(FPS)