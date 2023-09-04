

import pygame

class Words(pygame.sprite.Sprite):
    def __init__(self,fontType,size,x,y,text,colour):
            super().__init__()
            
            self.font = pygame.font.Font(fontType,size)
            self.image = self.font.render(text,True,colour)
            _,_,w,h = self.image.get_rect()
            self.rect = pygame.Rect(x,y,w,h)
            self.x = x
            self.y = y
    
    def write(self,screen):
          screen.blit(self.image,(self.rect))

    
            
