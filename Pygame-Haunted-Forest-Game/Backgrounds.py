import pygame
pygame.init()


class Backgrounds:
        def __init__(self, img_path):
           self.image = pygame.image.load(img_path)
           self.rect= self.image.get_rect()
        #    self.width = self.rect.width
        #    self.height= self.rect.height
           screenInfo= pygame.display.Info()
           self.width= screenInfo.current_w
           self.height=screenInfo.current_h
           








    