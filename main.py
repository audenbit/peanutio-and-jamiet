#:TO DO:
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
screen = pygame.display.set_mode((1280, 720))

frame_rate = 60


### Window customization ###

# fonts
main_font_path = os.path.join('assets', 'fonts', 'msg-font.ttf')
small_main_font = pygame.font.Font(main_font_path, 30)
medium_main_font = pygame.font.Font(main_font_path, 50)
big_main_font = pygame.font.Font(main_font_path, 70)

title_font_path = os.path.join('assets', 'fonts', 'big-font.ttf')
small_title_font = pygame.font.Font(title_font_path, 30)
medium_title_font = pygame.font.Font(title_font_path, 50)
big_title_font = pygame.font.Font(title_font_path, 70)

# Window Title
pygame.display.set_caption('Peanut and Jam')

# Sir Peanutio
peanutio_path = os.path.join('assets', 'peanutio.png')
peanutio_flip_path = os.path.join('assets', 'peanutio-flip.png')

# Grass Bkg
bkg_path = os.path.join('assets', 'ketchup&milk.png')

# Jamiet
jam_path = os.path.join('assets', 'pixil-frame-0 (9).png')
jam_img = pygame.image.load(jam_path)
jam_surf = pygame.Surface.convert_alpha(jam_img)
jam = pygame.transform.scale(jam_surf, (100, 100))

# Load bkg_path
bkg_surf = pygame.image.load(bkg_path)
bkg = pygame.transform.scale(bkg_surf, (1280,720))

icon = pygame.image.load(peanutio_path)
peanutio_flip = pygame.image.load(peanutio_flip_path)
pygame.display.set_icon(icon)

peanut_img = pygame.image.load(peanutio_path)
peanut_surf = pygame.Surface.convert_alpha(peanut_img)
peanut = pygame.transform.scale(peanut_surf, (100, 100))

txtbox_path = os.path.join('assets', 'textbox.png')
txtbox_img = pygame.image.load(txtbox_path)
txtbox_surf = pygame.Surface.convert_alpha(txtbox_img)
txtbox = pygame.transform.scale(txtbox_surf, (1200, 100))

fridge_path = os.path.join('assets', 'fridge.png')
fridge_img = pygame.image.load(fridge_path)
fridge_surf = pygame.Surface.convert_alpha(fridge_img)
fridge = pygame.transform.scale(fridge_surf, (1280, 720))

door_path = os.path.join('assets', 'door.png')
door_img = pygame.image.load(door_path)
door_surf = pygame.Surface.convert_alpha(door_img)
door = pygame.transform.scale(door_surf, (100, 100))

background = bkg

# fonts


#screen.blit(bkg_path)
screen.blit(background, (0, 0))
#mc = peanutio.Peanutio(peanutio_path,peanutio_flip_path, 100, bkg)


#jelly = peanutio.Food(jam_path, 10, bkg, 100)

#mc.position.x = 0  # go to x
#mc.position.y = 500 
line_color = (0, 0, 0)

class PeanutSprite(sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.speed = 100
    y = 100
    self.image = peanut.copy()
    self.rect = self.image.get_rect()#center = (1280, y))

  def move_left(self, game_window, background):
    game_window.blit(background, (self.rect.x, self.rect.y), self.rect)
    self.rect.x -= 100
    game_window.blit(peanutio_flip, (self.rect.x, self.rect.y))

  def move_right(self, game_window, background):
    game_window.blit(background, (self.rect.x, self.rect.y), self.rect)
    self.rect.x += 100
    game_window.blit(self.image, (self.rect.x, self.rect.y))
    display.update()

  def move_up(self, game_window, background):
    game_window.blit(background, (self.rect.x, self.rect.y), self.rect)
    self.rect.y -= 100
    game_window.blit(self.image, (self.rect.x, self.rect.y))

  def move_down(self, game_window, background):
    game_window.blit(background, (self.rect.x, self.rect.y), self.rect)
    self.rect.y += 100
    game_window.blit(self.image, (self.rect.x, self.rect.y))

class BackgroundTile(sprite.Sprite):
  def __init__(self, rect):
    super().__init__()
    self.effect = False
    self.rect = rect
  def give_effect(self, text):
    print(text)

tile_grid = []
tile_color = (255, 255, 255)
for row in range(8):
  row_of_tiles = []
  tile_grid.append(row_of_tiles)
  for column in range(13):
    tile_rect = Rect(100 * column, 100 * row, 100, 100)
    new_tile = BackgroundTile(tile_rect)
    row_of_tiles.append(new_tile)
    draw.rect(background, tile_color, (100 * column, 100 *row, 100, 100), 1)

class Level():
  def __init__(self, background, key_location, effect, text):
    self.background = background
    
mc = PeanutSprite()

# --------- Game Loop ------------
def main():
  background = bkg
  screen.blit(background, (0, 0))
  clock = time.Clock() 
  game_running = True
  quest = False
  level = 1
  
  while game_running:
    #screen.blit(background, (0, 0))

    clock.tick(frame_rate)

    for event in pygame.event.get():
        
      if event.type == pygame.KEYDOWN:
          if event.key == ord('a') :#or :
            mc.move_left(screen, background)    

          if event.key == ord('d'):
            mc.move_right(screen, background)

          if event.key == ord('s'):
            mc.move_down(screen, background)

          if event.key == ord('w'):
            mc.move_up(screen, background)

          x = mc.rect.x
          y = mc.rect.y

          tile_y = y//100
          tile_x = x//100

          tile_grid[tile_y][tile_x].effect = True 


          if level == 1:
            #screen.blit(jam, tile_grid[4][4])
            if tile_grid[4][6].effect == True or tile_grid[5][6] == True or tile_grid[3][6] == True :#or tile_grid[1][7]:
              ketchup_intro = small_main_font.render(" Ketchup: please help me check up on mustard. He is in",False, (0,0,0))
              ketchup_intro2 = small_main_font.render(" that door on the left", False, (0, 0, 0))
              #ketchup_intro3 =
              screen.blit(txtbox, (50, 610))
              screen.blit(ketchup_intro, (60, 605))
              screen.blit(ketchup_intro2, (60,635))
              screen.blit(door, tile_grid[0][0])
              quest = True
              tile_grid[4][3].effect= False
            if tile_grid[0][0].effect == True and quest == True:
              background = fridge
              print("In fridge!")
              screen.blit(background, (0, 0))
              screen.blit(mc.image, mc.rect)
              level = 2
          tile_grid[tile_y][tile_x].effect = False
            #tile_grid[4][3].effect= False
          if level == 2:
            pass
              
      if event.type == QUIT:
        pygame.quit()
    display.update()


  pygame.quit()

if __name__ == "__main__":
  main()