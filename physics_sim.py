import pygame

width = 300
height = 300

screen = pygame.display.set_mode((width, height))
screen.fill((255, 255, 255))
pygame.draw.circle(screen, (255, 0, 0), (150, 150), 15)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False