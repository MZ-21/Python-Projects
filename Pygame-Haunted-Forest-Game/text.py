import pygame

class TextBox(pygame.sprite.Sprite):
    def __init__(self, width, height, path, pos_x, pos_y):
        # calling parent class constructor of sprite
        super().__init__()
        self.image = pygame.image.load(path)

        #self.image = pygame.Surface([width, height])
        #self.image.fill(colour)  # changing the colour
        # getting the rectangle object of the image
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x-100, pos_y]
