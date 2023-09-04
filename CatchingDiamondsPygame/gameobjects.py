import pygame,random

class GameObject(pygame.sprite.Sprite):
    def __init__(self,x,y,img_path):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()  
        self.rect.center = (x,y)

        self.rand_xd = random.choice([-1,1])
        self.rand_yd = random.choice([-1,1])
 
    def update(self):
       self.rect = self.rect.move(self.rand_xd*self.speed,self.rand_yd*self.speed)

    


class Diamond(GameObject):
    def __init__(self,screen_rect,x):
        rand_x = random.randint(screen_rect.left +x,screen_rect.right-x) 
        rand_y = random.randint(x,screen_rect.height - x)
        super().__init__(rand_x,rand_y,"diamond.png" )
        self.speed = 5


class Spaceship(GameObject):
    def __init__(self, screen_rect):
        super().__init__(screen_rect.centerx, screen_rect.centery, 'spaceship.png')
        self.speed = 3

class Panes(pygame.sprite.Sprite):
    def __init__(self,width,height,colour,pos_x,pos_y):
        #calling parent class constructor of sprite
        super().__init__()
        #creating image for panes
        self.image = pygame.Surface([width,height])
        self.image.fill(colour) 
        #getting the rectangle object of the image
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

        
class updateO(GameObject):       
    def __init__(self):
        super().__init__()

    def update(self):
        super().update()
        
