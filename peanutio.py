import pygame
















'''class Peanutio:
  def __init__(self, sprite, flip_sprite, size, background, ):#position):
    self.sprite = sprite
    self.size = size
    self.background = background
    self.screen = pygame.display.set_mode((1280, 720))
    self.flip_sprite = flip_sprite
    peanut_img = pygame.image.load(self.sprite)
    peanut_surf = pygame.Surface.convert_alpha(peanut_img)
    self.image = pygame.transform.scale(peanut_surf, (self.size, self.size))
    flip_peanut_img = pygame.image.load(self.flip_sprite)
    flip_peanut_surf = pygame.Surface.convert_alpha(flip_peanut_img)
    self.image_flip = pygame.transform.scale(flip_peanut_surf, (self.size, self.size))
    self.screen.blit(self.image, (500, 200))
    self.position = self.image.get_rect()#center =(1280, 10))
    #self.flip_position = self.sprite_with_flip.get_rect()
  
  def move_right(self):
    self.screen.blit(self.image, self.position)
    pygame.display.update()
    
    for x in range(10):
      self.screen.blit(self.background, (0,0))
      self.position = self.position.move(10, 0) 
      self.screen.blit(self.image, self.position)
      pygame.display.update()
      #self.position = self.image.get_rect()
      pygame.time.delay(10)
      

  def move_left(self):
    self.screen.blit(self.image, self.position)
    pygame.display.update()
    for x in range(10):
      self.screen.blit(self.background, (0, 0))
      self.position = self.position.move(-10, 0)
      self.screen.blit(self.image_flip, self.position)
      pygame.display.update()
      #self.position = self.image.get_rect()
      pygame.time.delay(10)

  def move_up(self):
    self.screen.blit(self.image, self.position)
    pygame.display.update()
    for x in range(10):
      self.screen.blit(self.background, (0, 0))
      self.position = self.position.move(0, -10)
      self.screen.blit(self.image, self.position)
      pygame.display.update()
      #self.position = self.image.get_rect()
      pygame.time.delay(10)

  def move_down(self):
    self.screen.blit(self.image, self.position)
    pygame.display.update()
    for x in range(10):
      self.screen.blit(self.background, (0, 0))
      self.position = self.position.move(0, 10)
      self.screen.blit(self.image, self.position)
      pygame.display.update()
      #self.position = self.image.get_rect()
      pygame.time.delay(10)
'''
'''  def jump(self):
    y = 0
    self.screen.blit(self.image, self.position)
    for x in range(10):
      self.screen.blit(self.image, self.position)
      self.screen.blit(self.background, (0, 0))
      self.position = self.position.move(0, -y)
      self.screen.blit(self.image, self.position)
      pygame.display.update()
      y = -20*x + 80
      #self.position = self.image.get_rect()
      pygame.time.delay(15)

  def jump_right(self):
    y = 0
    self.screen.blit(self.image, self.position)
    for x in range(10):
      self.screen.blit(self.image, self.position)
      self.screen.blit(self.background, (0, 0))
      self.position = self.position.move(5, -y)
      self.screen.blit(self.image, self.position)
      pygame.display.update()
      y = -20*x + 80
      #self.position = self.image.get_rect()
      pygame.time.delay(15)

  def jump_left(self):
    y = 0
    self.screen.blit(self.image, self.position)
    for x in range(10):
      self.screen.blit(self.image, self.position)
      self.screen.blit(self.background, (0, 0))
      self.position = self.position.move(-5, -y)
      self.screen.blit(self.image_flip, self.position)
      pygame.display.update()
      y = -20*x + 80
      #self.position = self.image.get_rect()
      pygame.time.delay(15)
'''


'''class Food():
  def __init__(self, sprite, speed, background, size):
    self.sprite = sprite
    self.size = size
    self.background = background
    self.screen = pygame.display.set_mode((1280, 720))
    jar_img = pygame.image.load(self.sprite)
    jar_surf = pygame.Surface.convert_alpha(jar_img)
    self.image = pygame.transform.scale(jar_surf, (self.size, self.size))
    self.position = self.image.get_rect()

  def move(self):
    self.screen.blit(self.image, self.position)
    self.screen.blit(self.image, self.position)
    self.screen.blit(self.background, (0, 0))
    self.position = self.position.move(0, 10)
    self.screen.blit(self.image, self.position)
    pygame.display.update()
    pygame.time.delay(15)
    
  def spawn(self):
    self.position.x = random.randint(1, 900)
    
    
    '''