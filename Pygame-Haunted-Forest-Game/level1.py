from lib2to3.pytree import convert
#
from time import sleep, time
# from xxlimited import foo
import pygame
import Backgrounds, ChooseCharacter
# import Objects
import math
import random
import time, textWords, Objects

pygame.init()
# the background
level1BackGround = Backgrounds.Backgrounds("Pygame-Haunted-Forest-Game/images/level1.png")
screenLevelOne = pygame.display.set_mode(  # screen dimensions
    (1300, 800))  # pygame.resizable
    #1200 700

# the character
# the food
clock = pygame.time.Clock()
clock2 = pygame.time.Clock()
start = 1000

# creating a clock/timer
current_time = 0  # current time of clock
food_time = 0  # holds time of when food was made
rock_time = 0  # holds time of rocks being made
# number_food = 3 #value to hold amount food
number_of_rocks = 6 # value to hold number of rocks
number_hearts = 5
FPS = 100
rock_hits = 0
resetV = False
scroll = 0
win=False
rock_time = 0


def rock_text():
    rocks_count = "Hits: " + str(rock_hits)
    hits_font = textWords.Words("Pygame-Haunted-Forest-Game/fonts/block.ttf", 20, 10, 10, rocks_count, (0, 0, 0))
    hits_group = pygame.sprite.Group()
    hits_group.add(hits_font)
    hits_group.draw(screenLevelOne)
    hits_group.update()


def food_text():
    food_count = "coin: " + str(food_num)
    food_font = textWords.Words("Pygame-Haunted-Forest-Game/fonts/block.ttf", 20, 10, 50, food_count, (0, 0, 0))
    foodCount_group = pygame.sprite.Group()
    foodCount_group.add(food_font)
    foodCount_group.draw(screenLevelOne)
    foodCount_group.update()


def timer_text():
    timer_count = "Timer: " + str(start)[:2]
    time_font = textWords.Words("Pygame-Haunted-Forest-Game/fonts/block.ttf", 20, 10, 90, timer_count, (0, 0, 0))
    time_group = pygame.sprite.Group()
    time_group.add(time_font)
    time_group.draw(screenLevelOne)
    time_group.update()


number_food = 7 # value to hold amount food
# shift=0
food_Group = pygame.sprite.Group()  # food group
rock_group = pygame.sprite.Group()  # rock group
regenerate_rock_group = pygame.sprite.Group()
hero_Group = pygame.sprite.Group()  # the hero sprite
hits_group = pygame.sprite.Group()  # hit group
weapon_group = pygame.sprite.Group()

# loading heart image
lifeHeartGroup = pygame.sprite.Group()
heart_pos_x = 150
heart_pos_y = 50
# number_hearts = 3
heart_pos_x = screenLevelOne.get_width() - 200
heart_pos_y = 20
shift_heart = 0
shift_rock = 0


def makingObjects(type, number, x, y):
    global shift_heart

    if type == "food":
        for j in range(number):
            food_Group.add(Objects.Food(screenLevelOne.get_rect(), x, y))

    if type == "rocks":
        for p in range(number):
            
            rock_group.add(Objects.Rocks(screenLevelOne.get_rect(), None, y))

    if type == "hearts":
        for i in range(number):
            shift_heart -= x
            lifeHeartGroup.add(Objects.GameItems(
                heart_pos_x + shift_heart, heart_pos_y, "Pygame-Haunted-Forest-Game/images/lifeHeart.png"))

    if type == "hero":
        hero = Objects.Hero(screenLevelOne.get_rect())  # blitting the hero on the
        for i in range(number):
            hero_Group.add(hero)

    if type == "weapon":
        for w in range(number):
            weapon_group.add(Objects.weapon(screenLevelOne.get_rect(), x, y, "Pygame-Haunted-Forest-Game/images/axe.png", 3))


# for j in range(number_food):
#     food_Group.add(Objects.Food(level1BackGround.rect,0,0))

# initially making the game
makingObjects("food", number_food, 100, 0)
makingObjects("rocks", number_of_rocks, None, -500)
# makingObjects("hero", 1, None, None)

makingObjects("hearts", number_hearts, 50, None)

# bigR = Objects.GameObject(screenLevelOne.get_rect().width/2,0,"big_rock.png",(0,4),level1BackGround.rect)




# reset method
def reset():
    global rock_hits, FPS, resetV, shift_heart, start, food_num
    resetV = True
    rock_hits = 0
    shift_heart = 0
    food_num = 0

    makingObjects("rocks", 100, None, -500)

    # rock_time = pygame.time.get_ticks()


def winning():
    global rock_hits, FPS, resetV, shift_heart, start, food_num,win
    win = True
    food_Group.empty()
    rock_group.empty()
    rock_hits = 0
    shift_heart = 0
    food_num = 0
  
    makingObjects("weapon", 1, 300, 10)





# to get the number of backgrounds we neeed for endless scrolling
tiles = math.ceil((screenLevelOne.get_width()) / (level1BackGround.width))
print(tiles)

# the font
game_over = textWords.Words("Pygame-Haunted-Forest-Game/fonts/block.ttf", 60, (screenLevelOne.get_rect().width / 2)-200,
                            screenLevelOne.get_rect().centery, "GAME OVER", (0, 0, 0))
reset_text = textWords.Words("Pygame-Haunted-Forest-Game/fonts/block.ttf", 15, screenLevelOne.get_rect().centerx-100,
                             screenLevelOne.get_rect().centery+100 , "Press the space bar to restart",
                             (0, 0, 0))
rest_font_group = pygame.sprite.Group()  # creating font group
rest_font_group.add(game_over, reset_text)  # adding intro_font to font group

hit_by_rock = pygame.font.Font("Pygame-Haunted-Forest-Game/fonts/block.ttf", 30)
textX = 10  # text for hits x position
texty = 10  # text for hits y position

you_win = textWords.Words("Pygame-Haunted-Forest-Game/fonts/block.ttf", 60, (screenLevelOne.get_rect().width / 2)-200, screenLevelOne.get_rect().height / 2,
                          "YOU WIN!", (0, 0, 0))
collectW_text = textWords.Words("Pygame-Haunted-Forest-Game/fonts/block.ttf", 15, (screenLevelOne.get_rect().width / 2)-200,
                                (screenLevelOne.get_rect().height / 2) + (100), "COLLECT THE WEAPON TO UNLOCK LEVEL 2",
                                (0, 0, 0))
winning_font_Group = pygame.sprite.Group()
winning_font_Group.add(you_win, collectW_text)

rock_hits = 0
food_num = 0


def renderLevelOne():
    clock.tick(60)
    global scroll
    global rock_hits
    global shift_heart

    global scroll, rock_hits, shift_heart, food_num
    flipped_background = pygame.transform.flip(
        level1BackGround.image, False, True)

    for i in range(0, tiles + 1):
        screenLevelOne.blit(level1BackGround.image,
                            (i * level1BackGround.width + scroll, 0))

        lifeHeartGroup.draw(screenLevelOne)
        # bliting the food
        food_Group.draw(screenLevelOne)
        food_Group.update()

        # bliting the falling rock in the screen and making it fall from different places
        rock_group.draw(screenLevelOne)
        rock_group.update()
        

        ChooseCharacter.hero_group.draw(screenLevelOne)
        ChooseCharacter.hero_group.update()

        # drawing hearts onto screen
        lifeHeartGroup.draw(screenLevelOne)
        lifeHeartGroup.update()

        weapon_group.draw(screenLevelOne)
        weapon_group.update(300, 400)
    # reset scroll
    if abs(scroll) > level1BackGround.width:
        scroll = 0

        screenLevelOne.blit(flipped_background,
                            (level1BackGround.width, 0))

    for rock in rock_group:
        if rock.rect.top > screenLevelOne.get_height():
            rock.kill()
            makingObjects("rocks", 1, 0, -300)

    if resetV == True:
        rest_font_group.add(game_over, reset_text)
        rest_font_group.draw(screenLevelOne)
        rest_font_group.update()

    if win == True:
        winning_font_Group.add(you_win, collectW_text)
        winning_font_Group.draw(screenLevelOne)
        winning_font_Group.update()

    # creating and updating hit text
    # hits= hit_by_rock.render("Hits: "+ str(rock_hits), True, (0,0,0))
    # hits_group.update()
    # screenLevelOne.blit(hits, (textX,texty))
    # hits_group.draw(screenLevelOne)

    rock_text()
    food_text()
    timer_text()
    scroll -= 4
    pygame.display.flip()


def move():
    global resetV, start
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # Getting video system not initialized bc saying we didnt initialize even tho we called init

        # if key is pressed, do this
        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE] is True and resetV == True:  # if space is pressed
            rock_group.empty()
            food_Group.empty()
            print("space")
            resetV = False  # reset is false
            rest_font_group.empty()  # reset font group
            start = 1000

            # now re-making the level
            makingObjects("hearts", number_hearts, 50, None)
            makingObjects("food", number_food, 100, 0)
            makingObjects("rocks", number_of_rocks, 0, -500)
           



def collideLogic():
    global rock_hits
    global food_num
    global shift_heart,start
    #clock.tick(60)
    for heart in lifeHeartGroup.sprites():
        for sprite in rock_group.sprites():
            if pygame.sprite.groupcollide(rock_group, ChooseCharacter.hero_group, True, False):
                print("collided")
                rock_hits += 1
                if rock_hits == 2 or rock_hits == 4 or rock_hits == 6 or rock_hits == 8 or rock_hits == 10:
                    heart.kill()
                    sprite.kill()
                makingObjects("rocks", 1, 0, -500)
                hit_effect= pygame.mixer.music.load("Pygame-Haunted-Forest-Game/sound/hit.mp3")
                pygame.mixer.music.play(1)
            if pygame.sprite.groupcollide(food_Group, ChooseCharacter.hero_group, True, False):
                food_num += 1
                # food2=Objects.Food(level1BackGround.rect,10,0)
                # food_Group.add(food2)
                makingObjects("food", 1, 10, 0)
             

    if rock_hits == 10:
        rock_group.empty()  # removing old rocks
        food_Group.empty()
        lifeHeartGroup.empty()
        die_effect= pygame.mixer.music.load("Pygame-Haunted-Forest-Game/sound/oh!.mp3")
        pygame.mixer.music.play(1)

        reset()  # calling reset

    if start != 0:
        start -= 1
    if start == 0 and resetV == False and win==False:
        rock_group.empty()  # removing old rocks
        food_Group.empty()
        lifeHeartGroup.empty()

        reset()

    if food_num == 20:
        rock_group.empty()  # removing old rocks
        food_Group.empty()
        lifeHeartGroup.empty()
        start = 0
        winning()
# test test

running = True

      