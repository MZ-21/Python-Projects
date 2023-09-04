import pygame, time, random
import gameobjects

pygame.init()

# Initialize the game
panel_width = 150
panel_height = 600
bg_img = pygame.image.load('background.jpg')
bg_rect = bg_img.get_rect() #getting rectangle object of bg image
bg_rect.height = panel_height


screen = pygame.display.set_mode((bg_rect.width, panel_height)) #setting the width and height of the screen
screen_rect = screen.get_rect() #getting rectangle object of the screen
inner_rect = screen_rect.copy()
inner_rect.left += panel_width
inner_rect.width -= 2*panel_width


no_of_diamonds = 10
diamond_group = pygame.sprite.Group()
for i in range(no_of_diamonds):
   diamond_group.add(gameobjects.Diamond(inner_rect,50))

no_of_spaceships = 1
spaceship_group = pygame.sprite.Group()
for i in range(no_of_spaceships):
   spaceship_group.add(gameobjects.Spaceship(inner_rect))
   



#adding panels
panel1 = gameobjects.Panes(panel_width,panel_height,(109, 195, 203, 1),0,0)
panel2 = gameobjects.Panes(panel_width,panel_height,(109, 195, 203, 1),850,0)


panel1.rect.topleft = panel1.rect.topleft #setting panel to top left corner of the screen
#panel2.rect.x= 850 #setting panel to top right corner of screen
pane_group = pygame.sprite.Group() #creating sprite group
pane_group.add(panel1,panel2)

#group of saved and taken sprites
pane_saved=pygame.sprite.Group()

pane_taken = pygame.sprite.Group()





#adding font
font = pygame.font.Font("CoffeeHealing.ttf",25)

#number of taken or saved that will be updated
number_taken = 0
number_saved = 0




def render():

    screen.blit(bg_img,bg_rect)
    diamond_group.update()
    diamond_group.draw(screen)
      
    #adding font 
    taken = font.render("Taken: " + str(number_taken) ,True,(0,0,0)) #adding font to blit onto panel1
    saved= font.render("Saved: " + str(number_saved),True,(0,0,0)) #adding font to blit onto panel2
 
    
    pane_saved.update()
    pane_saved.draw(panel2.image) #drawing saved diamonds on panel2
    

    pane_taken.update()
    pane_taken.draw(panel1.image) #drawing taken diamonds on panel1


    spaceship_group.update() #updating spaceships
    spaceship_group.draw(screen) #drawing changed spaceships onto screen
    pane_group.draw(screen) #drawing pane on screen
    
    
    screen.blit(taken,(10,10)) #adding the font over the screen
    screen.blit(saved,(screen_rect.width-125,10)) #adding font on panel2
    
    


    pygame.display.flip()

render()

running = True
# gameloop
while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for sprite in diamond_group.sprites():
                if sprite.rect.collidepoint(event.pos): #if it collides with mouse clicked

                   
                    sprite.rand_xd= 0 #stopping movement in x dir
                    sprite.rand_yd= 0 #stopping movement in y dir
                    sprite.rect.x = random.randint(0,50) #randomly generating it on panel2 x-dir
                    sprite.rect.y = random.randint(0,200) #randomly generating spot on panel2 in y-dir

                    pane_saved.add(sprite) #adding sprite to saved group
                    
                    diamond_group.remove(sprite)#remove sprite
                    number_saved += 1 #increase amount saved
                    diamond_group.update()
                    diamond_group.draw(screen)
                    
                        

    
    #game logic


    for sprites in diamond_group.sprites():
        for spaceship in spaceship_group.sprites():
           if pygame.sprite.groupcollide(diamond_group,spaceship_group,True,False): #if diamond and spaceship collide, kill diamond
             
              number_taken+=1 #increasing amount taken 
              
              takenDiamond = gameobjects.Diamond(panel1.rect,50)
              takenDiamond.rand_xd= 0 #stopping movement of sprite taken in the x-dir
              takenDiamond.rand_yd= 0 #stopping movement of sprite taken in the y-dir
              
              pane_taken.add(takenDiamond) #adding sprite to taken group
            

    
    for spaceship in spaceship_group.sprites(): #iterating through the spaceship
        if spaceship.rect.colliderect(panel1.rect) or spaceship.rect.colliderect(panel2.rect):
            spaceship.rand_xd = spaceship.rand_xd*(-1) #reversing the direction if spaceship collides with panels or upper/lower bounds
            
        if spaceship.rect.bottom >= screen_rect.bottom or spaceship.rect.top <=screen_rect.top:
            spaceship.rand_yd = spaceship.rand_yd*(-1)
            

            

    for diamonds in diamond_group.sprites():
        if diamonds.rect.colliderect(panel1.rect) or diamonds.rect.colliderect(panel2.rect):
            diamonds.rand_xd = diamonds.rand_xd*(-1) #reversing direction of diamonds if it collides with panels or bounds


        if diamonds.rect.bottom >= screen_rect.bottom or diamonds.rect.top <= screen_rect.top:
            diamonds.rand_yd = diamonds.rand_yd*(-1)
   

    #render
    render()
    time.sleep(0.05) #creating a delay to see movement

pygame.quit()

