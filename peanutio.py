import pygame


class Peanutio:
    def __init__(self, sprite, size):
        self.sprite = sprite
        self.size = size
        peanut_img = pygame.image.load(self.sprite)
        peanut_surf = pygame.Surface.convert_alpha(peanut_img)
        self.image = pygame.transform.scale(
            peanut_surf, (self.size, self.size))
        self.position = self.image.get_rect()

    def move_right(self):
        screen.blit(self.image, self.position)
        display.update()
        for x in range(100):
            screen.fill(bkg)
            self.position = mc.position.move(4, 0)
            screen.blit(self.image, self.position)
            display.update()
            time.delay(50)
