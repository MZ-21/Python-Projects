#only use this class to test object methods so we know how to implement them in the actual game
#currently jump has been implemented + works
#l/r movement works

import pygame
import time
import Objects

pygame.init()

screen = pygame.display.set_mode((800,600))
screen_rect = screen.get_rect()
print(screen_rect.width)
hero = Objects.Hero(screen_rect)
enemy = Objects.Enemy(screen_rect)

#render screen definition
def render():
    screen.fill((100,234,25),screen_rect,0)
    screen.blit(hero.image, hero.rect)
    screen.blit(enemy.image,enemy.rect)
    enemy.slide()
    if hero.jumppos == 0:
        hero.jump("up")
    pygame.display.flip()

running = True
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                hero.jump("down")
            if event.key == pygame.K_LEFT:
                hero.left()
            elif event.key == pygame.K_RIGHT:
                hero.right()
    
    #render screen
    render()
    time.sleep(0.05)



pygame.quit()