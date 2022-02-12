#TO DO:
# mc CLass to store things like health movment speed ect.



# imports
import pygame
from pygame import *
import os
import peanutio
#from random import randint
# initializes pygame to run
pygame.init()

#clock = time.Clock()
# create the screen
screen = pygame.display.set_mode((900, 400))

frame_rate = 60

# Window customization 
pygame.display.set_caption('Peanut and Jam')
peanutio_path = os.path.join('assets', 'peanutio.png')
icon = pygame.image.load(peanutio_path)
pygame.display.set_icon(icon)
bkg = (0, 0, 0)
screen.fill(bkg)

#Set up peanutio image
#peanut_img = image.load(peanutio_path)
#peanut_surf = Surface.convert_alpha(peanut_img)
#peanutio = transform.scale(peanut_surf, (100, 100))
#peanutio_position = peanutio.get_rect()
#screen.blit(peanutio, (100, 100))
mc = peanutio.Peanutio(peanutio_path, 100)

#Getting movment set up
'''screen.blit(mc.image, mc.position)
display.update()
for x in range(100):
  screen.fill(bkg)
  mc.position = mc.position.move(4, 0)
  screen.blit(mc.image, mc.position)
  display.update()
  time.delay(50)'''
mc.move_right()
#display.update()
# --------- Game Loop ------------
def main():
  clock = time.Clock()
  game_running = True
  while game_running:
    clock.tick(frame_rate)
    for event in pygame.event.get():
      if event.type == QUIT:
            game_running = False

    display.update()

  pygame.quit()

if __name__ == "__main__":
  main()