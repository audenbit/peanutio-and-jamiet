# imports
import pygame

# initializes pygame to run
pygame.init() 

# create the screen
screen = pygame.display.set_mode((1000, 650))

# loop so it doesnt automatically close
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Window title
pygame.display.set_caption('Peanutio and Jamiet')