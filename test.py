import pygame
from Character import Character
pygame.init()

screen = pygame.display.set_mode([2000, 1200])
c1 = Character(1000, [10-20])
c2 = Character(1100, [8-18])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))

    c1.get_damage(1)
    c2.get_damage(2)

    pygame.draw.circle(screen, (0, 0, 255), (1000, 600), 75)
    pygame.draw.rect(screen, (100, 100, 100), (400, 100, 100, 1000), 0)
    pygame.draw.rect(screen, (100, 100, 100), (1500, 100, 100, 1000), 0)
    pygame.draw.rect(screen, (0, 255, 255), (400, 100 + int(1000 * (1-c1.life_percent())), 100, int(1000*c1.life_percent())), 0)
    pygame.draw.rect(screen, (0, 255, 0), (1500, 100 + int(1000 * (1-c2.life_percent())), 100, int(1000*c2.life_percent())), 0)

    pygame.display.flip()

pygame.quit()