import pygame

width = 300
height = 300

# Parameters for the window
screen = pygame.display.set_mode((width, height))
screen.fill((255, 255, 255))

# Creates an object.
class Particle(object):
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.colour = (255, 0, 0) #
        self.speed = -0.01
        self.accel = -0.00001
    
    def display(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size)
    
    def move(self):
        self.y -= self.speed
    
    def accelerate(self):
        self.speed += self.accel

    # Bounce
    def bounce(self):
        if self.y > height - self.size:
            self.speed = -(self.speed - (self.speed/100)*4)
        
        elif self.y < self.size:
            self.speed = -(self.speed - (self.speed/100)*4)

# Water
rect = pygame.Surface((1000,1000), pygame.SRCALPHA, 32)
rect.fill((0, 0, 255, 50))
screen.blit(rect, (300,300))

# Initializes boat object.
boat = Particle(150, 150, 15)

# Opens the window.
pygame.display.flip()

# Keeps the window running until it's closed.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))
    boat.move()
    boat.accelerate()
    boat.bounce()
    boat.display()
    pygame.display.flip()