   #:TO DO:
# mc CLass to store things like health movment speed ect.

# imports
import pygame
from pygame import *
import os
#import peanutio
from time import sleep
#from random import randint
# initializes pygame to run
pygame.init()
#clock = time.Clock()
# create the screen
HEIGHT = 1280
WIDTH = 720

screen = pygame.display.set_mode((HEIGHT, WIDTH))

frame_rate = 60


### Window customization ###
# Win size


# fonts
main_font_path = os.path.join('assets', 'fonts', 'msg-font.ttf')
small_main_font = pygame.font.Font(main_font_path, 25)
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

# Jam
jam_path = os.path.join('assets', 'jam.png')
jam_img = pygame.image.load(jam_path)
jam_surf = pygame.Surface.convert_alpha(jam_img)
jam = pygame.transform.scale(jam_surf, (100, 100))



# Load bkg_path
bkg_surf = pygame.image.load(bkg_path)
bkg = pygame.transform.scale(bkg_surf, (HEIGHT, WIDTH))

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
fridge = pygame.transform.scale(fridge_surf, (HEIGHT, WIDTH))

door_path = os.path.join('assets', 'door.png')
door_img = pygame.image.load(door_path)
door_surf = pygame.Surface.convert_alpha(door_img)
door = pygame.transform.scale(door_surf, (100, 100))

mustard_path = os.path.join('assets', 'MustardScreen.png')
mustard_img = pygame.image.load(mustard_path)
mustard_surf = pygame.Surface.convert_alpha(mustard_img)
mustard = pygame.transform.scale(mustard_surf, (HEIGHT, WIDTH)) 

locked_door_path = os.path.join('assets', 'locked_door.png')
locked_door_img = pygame.image.load(locked_door_path)
locked_door_surf = pygame.Surface.convert_alpha(locked_door_img)
locked_door = pygame.transform.scale(locked_door_surf, (100, 100)) 

cheese_screen_path = os.path.join('assets', 'cheese_screen.png')
cheese_screen_img = pygame.image.load(cheese_screen_path)
cheese_screen_surf = pygame.Surface.convert_alpha(cheese_screen_img)
cheese_screen = pygame.transform.scale(cheese_screen_surf, (1280, 720)) 

jail_withjam_path = os.path.join('assets', 'jail_withjam.png')
jail_withjam_img = pygame.image.load(jail_withjam_path)
jail_withjam_surf = pygame.Surface.convert_alpha(jail_withjam_img)
jail_withjam = pygame.transform.scale(jail_withjam_surf, (1280, 720)) 

gun_path = os.path.join('assets', 'gun.png')
gun_img = pygame.image.load(gun_path)
gun_surf = pygame.Surface.convert_alpha(gun_img)
gun = pygame.transform.scale(gun_surf, (20, 20)) 

lazer_path = os.path.join('assets', 'lazer.png')
lazer_img = pygame.image.load(lazer_path)
lazer_surf = pygame.Surface.convert_alpha(lazer_img)
lazer = pygame.transform.scale(lazer_surf, (10, 10)) 

dead_jam_path = os.path.join('assets', 'dead_jam.png')
dead_jam_img = pygame.image.load(dead_jam_path)
dead_jam_surf = pygame.Surface.convert_alpha(dead_jam_img)
dead_jam = pygame.transform.scale(dead_jam_surf, (100, 100)) 


jail_nojam_path = os.path.join('assets', 'jail_nojam.png')
jail_nojam_img = pygame.image.load(jail_nojam_path)
jail_nojam_surf = pygame.Surface.convert_alpha(jail_nojam_img)
jail_nojam = pygame.transform.scale(jail_nojam_surf, (1280, 720))

jamiet_path = os.path.join('assets', 'jamiet.png')
jamiet_img = pygame.image.load(jamiet_path)
jamiet_surf = pygame.Surface.convert_alpha(jamiet_img)
jamiet = pygame.transform.scale(jamiet_surf, (100, 100))

# fonts

background = bkg
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
  clock = pygame.time.Clock() 
  game_running = True
  quest = False
  milk_quest = False
  cheeso_quest = False
  mustard_door = False
  level = 1
  half_key1 = False
  half_key2 = False
  jelly_fight = False
  she_dead = False
  
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
            #screen.blit(door, tile_grid[0][0])
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(600, 400, 100, 100), 2)
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(900, 100, 100, 100), 2)
            screen.blit(locked_door, tile_grid[0][7])
            #screen.blit(jam, tile_grid[4][4])
            if tile_grid[4][6].effect == True or tile_grid[5][6] == True or tile_grid[3][6] == True :#or tile_grid[1][7]:
              if mustard_door == False:
                  ketchup_intro= small_main_font.render(" Ketchup: Can you check up on my brother Mustard? He is in", False, (0, 0, 0))
                  ketchup_intro2 = small_main_font.render(" that door on the left", False, (0, 0, 0))
                  screen.blit(txtbox, (50, 610))
                  screen.blit(ketchup_intro, (60, 605))
                  screen.blit(ketchup_intro2, (60,635))
                  screen.blit(door, tile_grid[0][0])
                  quest = True
                  tile_grid[0][0].effect= False

              else:
                ketchup_outro = small_main_font.render("Thanks for checking up on him, here have your half key.", False, (0,0, 0))
                screen.blit(txtbox, (50, 610))
                screen.blit(ketchup_outro, (60, 605))
                half_key1 = True
			

            if tile_grid[0][0].effect == True and quest == True:
              background = mustard
              #print("In fridge!")
              screen.blit(background, (0, 0))
              mc.rect.x = 1000
              mc.rect.y = 500
              screen.blit(mc.image, mc.rect)
              #screen.blit(door, (1000, 500))
              level = 2
          #tile_grid[tile_y][tile_x].effec
            if tile_grid[1][9].effect == True:
              if cheeso_quest == False:
                milk_intro= small_main_font.render(" Milk: Can you check up on my son Cheeso? He is in that door on the", False, (0, 0, 0))
                milk_intro2 = small_main_font.render(" right. I need to know if he\'s at school", False, (0, 0, 0))
                screen.blit(txtbox, (50, 610))
                screen.blit(milk_intro, (60, 605))
                screen.blit(milk_intro2, (60,635))
                screen.blit(door, tile_grid[0][11])
                milk_quest = True
              else:
                milk_outro = small_main_font.render(" Milk: well thanks for chenking on him. I\'ll have to have a talk with him ", False, (0, 0, 0))
                milk_outro2 = small_main_font.render(" about this later. Anyways, heres your half key for that door", False, (0, 0, 0))
                screen.blit(txtbox, (50, 610))
                screen.blit(milk_outro, (60, 605))
                screen.blit(milk_outro2, (60, 635))
                half_key2 = True
                
            if tile_grid[0][11].effect == True and milk_quest == True:
              #print("CHEESE!")
              background = cheese_screen
              screen.blit(background, (0, 0))
              mc.rect.x = 0
              mc.rect.y = 500
              screen.blit(mc.image, mc.rect)
              level = 3

            if tile_grid[0][7].effect == True and half_key1 == True and half_key2 == True:
              level = 4
              background = jail_withjam
              screen.blit(background, (0, 0))
              mc.rect.x = 0
              mc.rect.y = 600
              screen.blit(mc.image, mc.rect)
              
                                                      
          if level == 2:
            screen.blit(door, tile_grid[5][10])
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(400, 400, 100, 100), 2)
            if tile_grid[4][4].effect == True or tile_grid[1][3] == True:#True or tile_grid[3][3]:
              #print("effect triggered")
              mustard_txt = small_main_font.render(" Mustard: Oh my brother wants to know how im doing? At",False, (0,0,0))
              mustard_txt2 = small_main_font.render(" least somebody does. Well all the other", False, (0, 0, 0))
              mustard_txt3 = small_main_font.render(" condiments have been used up so im all alone", False, (0, 0, 0))
              #peanutio_mustard_txt =small_main_font.render(" Peanutio: Sup Mustard, hows it going", False, (0, 0, 0))
			  
              #screen.blit(txtbox, (50, 610))
              #sleep(0.7)
              
              #screen.blit(peanutio_mustard_txt, (60, 605))
              #sleep(2)
              screen.blit(txtbox, (50, 610))
              screen.blit(mustard_txt, (60, 605))
              screen.blit(mustard_txt2, (60,635))
              screen.blit(mustard_txt3, (60, 665))
              #screen.blit(door, tile_grid[5][10])
              #screen.blit(door, tile_grid[5][6])
              mustard_door = True
            if mustard_door == True and tile_grid[5][10].effect == True:
              level = 1
              background = bkg
              mc.rect.x = 0
              mc.rect.y = 0
              screen.blit(background, (0, 0))
              screen.blit(mc.image, mc.rect)
              
          if level == 3:
            screen.blit(door, tile_grid[5][0])
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(800, 500, 100, 100), 2)
            if tile_grid[5][8].effect == True:
              cheeso_txt = small_main_font.render(" Cheeseo: My dad wants to know if im in school? Thats funny. ",False, (0,0,0))
              cheeso_txt2 = small_main_font.render(" I dont remember saying i would quit my super awsome one person band",False, (0,0,0))
              cheeso_txt3 = small_main_font.render(" for \'school\'", False, (0, 0, 0))
              screen.blit(txtbox, (50, 610))
              screen.blit(cheeso_txt, (60, 605))
              screen.blit(cheeso_txt2, (60,635))
              screen.blit(cheeso_txt3, (60, 665))
              cheeso_quest = True
            if cheeso_quest == True and tile_grid[5][0].effect == True:
              level = 1
              background = bkg
              mc.rect.x = 1100
              mc.rect.y = 0
              screen.blit(background, (0, 0))
              screen.blit(mc.image, mc.rect)
          if level == 4:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(900, 600, 100, 100), 2)
            if she_dead == False:  
              if tile_grid[6][9].effect == True:
                screen.blit(jam, (tile_grid[2][12]))
                jam_txt = small_main_font.render(" Jelly: you will never get Jam back! I\'m done being the #2 sweet sprea d!",False, (0,0,0))
                jam_txt2 = small_main_font.render(" And you, peanut, that doesnt even make sense. have you ever heard of a ",False, (0,0,0))
                jam_txt3 = small_main_font.render(" peanutbutter and JAM sandwich?? WE WERE MEANT FOR EACH OTHER", False, (0, 0, 0))
                screen.blit(txtbox, (50, 100))
                screen.blit(jam_txt, (60, 103))
                screen.blit(jam_txt2, (60, 125))
                screen.blit(jam_txt3, (60, 145))
                jelly_fight = True
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(1100, 200, 100, 100), 2)
              elif tile_grid[2][11].effect == True and jelly_fight == True:
                print("final scene")              
                screen.blit(background, (0, 0))
                screen.blit(mc.image, mc.rect)
                screen.blit(dead_jam, tile_grid[2][12])
                peanutio_txt = small_main_font.render(" Peanut: I will free you Jam!!", False, (0, 0, 0))
                screen.blit(txtbox, (60, 610))
                screen.blit(peanutio_txt, (60, 605))
                screen.blit(gun, (1130, 250))
                she_dead = True
            else:
              screen.blit(background, (0,0))
              screen.blit(dead_jam, tile_grid[2][12])
              screen.blit(mc.image, mc.rect)
              pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(900, 600, 100, 100), 2)
              if tile_grid[6][9].effect == True:
                screen.blit(jam, (tile_grid[2][12]))
                jamiet_txt = small_main_font.render(" Jam: OMG i love you lmao ;) ~~",False, (0,0,0))
                based_txt = small_main_font.render(" Peanut: WOWOW me too, unfortunatly i seek only vengence YOLO :)",False, (0,0,0))
                screen.blit(jail_nojam, (0, 0))
                screen.blit(mc.image, mc.rect)
                screen.blit(jamiet, (900, 600))
                screen.blit(txtbox, (50, 100))
                screen.blit(jamiet_txt, (60, 103))
                screen.blit(txtbox, (60, 610))
                screen.blit(based_txt, (60, 605))

			  
            
			      #elif she_dead = True:
				    #screen.blit
          
          tile_grid[tile_y][tile_x].effect = False
          

        
          if event.type == QUIT:
            pygame.quit()

    display.update()


  pygame.quit()

if __name__ == "__main__":
  main()