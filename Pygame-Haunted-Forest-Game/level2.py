from operator import truediv
import pygame

import Backgrounds
import Objects
import math
import random
import Objects
import time
import textWords
import ChooseCharacter

pygame.init()

start = pygame.time.get_ticks()


# the background------------------------

level2background = pygame.image.load(
    "Pygame-Haunted-Forest-Game/images/level2Resized.png")
level2bg = pygame.transform.scale(
    level2background, (level2background.get_width()*0.8, level2background.get_height()*0.8))
lvl2Background = Backgrounds.Backgrounds(
    "Pygame-Haunted-Forest-Game/images/level2Resized.png")
resetV = False

level2BackGround = Backgrounds.Backgrounds(
    "Pygame-Haunted-Forest-Game/images/level2scaled.png")

screenLevelOne = pygame.display.set_mode(
    (1300, 800))
screenRect = screenLevelOne.get_rect()

# font-----------------------------------------------------------------
font = pygame.font.Font("Pygame-Haunted-Forest-Game/fonts/block.ttf", 34)
secondfont = pygame.font.Font(
    "Pygame-Haunted-Forest-Game/fonts/CoffeeHealing.ttf", 30)

# the hero stuff---------------------------------------------------------
#theHero = Objects.Hero(screenRect)


for heroes in ChooseCharacter.hero_group.sprites():
    if(heroes.string == "Pygame-Haunted-Forest-Game/images/hiker.png"):

        theHero = Objects.Hero(
            screenRect, "Pygame-Haunted-Forest-Game/images/hiker.png")
        print("hero1")
        ChooseCharacter.hero_group.empty()
        theHero.rect.y = 500
        ChooseCharacter.hero_group.add(theHero)

    if heroes.string == "Pygame-Haunted-Forest-Game/images/hero(1).png":
        theHero = Objects.Hero(
            screenRect, "Pygame-Haunted-Forest-Game/images/hero(1).png")
        print("hero2")
        ChooseCharacter.hero_group.empty()
        theHero.rect.y = 500
        ChooseCharacter.hero_group.add(theHero)

theHero_speed = 7


# the weapon group ---------------------------------------------------------

weapon_group = pygame.sprite.Group()


# loading heart image---------------------------------------------------------------
lifeHeartGroup = pygame.sprite.Group()
number_hearts = 4
heart_pos_x = 200
heart_pos_y = 100
shift_heart = 0

for i in range(number_hearts):
    lifeHeartGroup.add(Objects.GameItems(
        200+shift_heart, 100, "Pygame-Haunted-Forest-Game/images/lifeHeart.png"))
    shift_heart += 50


clock = pygame.time.Clock()
FPS = 60

# game text -------------------------------------------------------------------------

game_over = textWords.Words("Pygame-Haunted-Forest-Game/fonts/block.ttf", 60, screenLevelOne.get_rect(
).width/2-(280), (screenLevelOne.get_rect().height/2)-50, "GAME OVER", (255, 255, 255))
reset_text = textWords.Words("Pygame-Haunted-Forest-Game/fonts/block.ttf", 15, screenLevelOne.get_rect(
).width/2-(220), (screenLevelOne.get_rect().height/2)+50, "Press the space bar to restart", (255, 255, 255))
winner = textWords.Words("Pygame-Haunted-Forest-Game/fonts/block.ttf", 60, screenLevelOne.get_rect(
).width/2 - (460), screenLevelOne.get_rect().height/2-50, "Congratulations!", (255, 255, 255))
completion_text = textWords.Words("Pygame-Haunted-Forest-Game/fonts/block.ttf", 15, screenLevelOne.get_rect(
).width/2-(215), (screenLevelOne.get_rect().height/2)+50, "You have completed your quest", (255, 255, 255))

global lose, win
lose = False
win = False


# creating font groups ---------------------------------------------------------------
rest_font_group = pygame.sprite.Group()  # creating font group
rest_font_group.add(game_over, reset_text)  # adding intro_font to font group
winning_font_Group = pygame.sprite.Group()
winning_font_Group.add(winner)

key = pygame.key.get_pressed()


# to get the number of backgrounds we neeed for endless scrolling--------------------
tiles = math.ceil((screenLevelOne.get_width()) / (level2BackGround.width))
# print(tiles)
scroll = 0


lifeHeartGroup.draw(screenLevelOne)
ChooseCharacter.hero_group.draw(screenLevelOne)

# weapon_group.draw(screenLevelOne)


# enemy groups-----------------------------------------------------------------------
enemy_group = pygame.sprite.Group()

# appears from the right
enemies_group = pygame.sprite.Group()
number_enemies = 5
enemies_left = number_enemies
x_pos = 1550
y_pos = 500
increment_x = 0

global score
score = 0

#theEnemy = Objects.enemyAnimation(x_pos + increment_x, y_pos, [-9, 0])

for i in range(number_enemies):
    enemies_group.add(Objects.enemyAnimation(
        x_pos + increment_x, y_pos, [-2, 0]))
    increment_x += 650

enemy_hits_right = 0
enemy_hits_left = 0
#score = 0

# appears from the left
enemy_groupReverse = pygame.sprite.Group()
xpos = -700
ypos = 500
increment_x = 0

for i in range(number_enemies):
    enemy_groupReverse.add(Objects.enemyAnimationReverse(
        xpos + increment_x, ypos, [2, 0]))
    increment_x += 500

#score = 0

delay_time2 = 7000  # to wait for the enemies to appear

win_flag = False


def winning():
    global win, win_flag
    if not enemies_group and not enemy_groupReverse and lifeHeartGroup:

        win = True
        enemies_group.empty()
        enemy_groupReverse.empty()
        lifeHeartGroup.empty()
        if not lifeHeartGroup:
            makingObjects("ring", 1, 300, 10)


def renderLevel2():
    clock.tick(FPS)
    global scroll
    flipped_background = pygame.transform.flip(
        level2BackGround.image, False, True)

    for i in range(0, tiles+1):

        screenLevelOne.blit(level2BackGround.image,
                            (i * level2BackGround.width + scroll, 0))
        lifeHeartGroup.draw(screenLevelOne)
        ChooseCharacter.hero_group.draw(screenLevelOne)

        if theHero.jumppos == 1:
            theHero.jump("down")

        lifeHeartGroup.draw(screenLevelOne)
        # hero.draw(screenLevelOne)
        if theHero.jumppos == 1:
            theHero.jump("down")
        weapon_group.draw(screenLevelOne)

        currentTime = pygame.time.get_ticks()
        if currentTime - start > delay_time2:
            # pygame.time.wait(400)
            enemies_group.update(screenLevelOne)
            enemies_group.draw(screenLevelOne)
            # pygame.time.wait(400)
            enemy_groupReverse.update(screenLevelOne)
            enemy_groupReverse.draw(screenLevelOne)

        # reset scroll
        if abs(scroll) > level2BackGround.width:
            scroll = 0
            screenLevelOne.blit(flipped_background,
                                (level2BackGround.width, 0))

        for heart in lifeHeartGroup:
            if heart == 0:
                lose_end_Screen()

        if lose == True:
            rest_font_group.add(game_over, reset_text)
            rest_font_group.draw(screenLevelOne)
            rest_font_group.update()
            # lose_effect = pygame.mixer.music.load("oh!.mp3")
            # pygame.mixer.music.play(1)

        if win == True:
            winning_font_Group.add(winner, completion_text)
            winning_font_Group.draw(screenLevelOne)
            winning_font_Group.update()
            ring_group.draw(screenLevelOne)
            ring_group.update(500, 500)

        hello = font.render("score: " + str(score),
                            False, (255, 255, 255), None)
        hello_rect = hello.get_rect()
        hello_rect.x = 205
        hello_rect.y = 55
        screenLevelOne.blit(hello, hello_rect)

    theHero.update()
    scroll -= 4
    pygame.display.flip()


def lose_end_Screen():
    global lose, lose_effect
    lose = True


def win_end_screen():
    global win
    win = True


delay_time = 7000
global hero_hits
hero_hits = 0


def setUpScreenMain():
    screenLevelOne.blit(level2BackGround.image, level2BackGround.rect)

    lifeHeartGroup.draw(screenLevelOne)
    ChooseCharacter.hero_group.draw(screenLevelOne)
    currentTime = pygame.time.get_ticks()
    if currentTime - start > delay_time:
        # print("hello")
        enemies_group.draw(screenLevelOne)
        enemy_groupReverse.draw(screenLevelOne)


def sprite_events():
    for enemy in enemies_group.sprites():
        for enemy in enemy_groupReverse.sprites():
            for heart in lifeHeartGroup.sprites():

                if pygame.sprite.groupcollide(ChooseCharacter.hero_group, enemies_group, False, True):
                    score -= 2
                    hero_hits += 1
                    heart.kill()
                    enemy_effect = pygame.mixer.music.load(
                        "Pygame-Haunted-Forest-Game/sound/enemyKill.wav")
                    pygame.mixer.music.play(1)

                elif pygame.sprite.groupcollide(ChooseCharacter.hero_group, enemy_groupReverse, False, True):
                    score -= 2
                    hero_hits += 1
                    heart.kill()
                    enemy_effect = pygame.mixer.music.load(
                        "Pygame-Haunted-Forest-Game/sound/enemyKill.wav")
                    pygame.mixer.music.play(1)

                elif heart == 0:
                    lose_end_Screen()

    for w in weapon_group.sprites():
        if pygame.sprite.groupcollide(weapon_group, enemies_group, True, False):
            enemy_hits += 1
            score += 1
            w.kill()
            enemies_group.add(Objects.enemyAnimation(
                x_pos + increment_x, y_pos, [-3, 0]))
        enemies_group.draw(screenLevelOne)

    if enemy_hits == 3:
        score += 4
        enemy.kill()
        clock.tick(80)
        enemy_hits = 0

    for w in weapon_group:
        if w.dir == "right":
            w.rightupdate()
        else:
            w.leftupdate()


running = True


ring_group = pygame.sprite.Group()


def makingObjects(type, number, x, y):
    global shift_heart
    global increment_x, theHero

    if type == "weaponRight":
        for p in range(number):

            weapon_group.add(theHero.throwR(screenRect))

    if type == "hearts":
        shift_heart = 0
        for i in range(number):
            lifeHeartGroup.add(Objects.GameItems(
                heart_pos_x + shift_heart, heart_pos_y, "Pygame-Haunted-Forest-Game/images/lifeHeart.png"))
            shift_heart += 50

    if type == "hero":
        # hero = Objects.Hero(screenLevelOne.get_rect())  # blitting the hero on the
        for i in range(number):
            ChooseCharacter.hero_group.add(theHero)

    if type == "weaponLeft":
        for w in range(number):
            weapon_group.add(theHero.throwL(screenRect))

    if type == "enemyRight":
        increment_x = 0
        for p in range(number):
            enemies_group.add(Objects.enemyAnimation(
                x_pos + increment_x, y_pos, [-3, 0]))
            increment_x += 450

    if type == "enemyLeft":
        increment_x = 0
        for p in range(number):
            enemies_group.add(Objects.enemyAnimationReverse(
                xpos - increment_x, ypos, [3, 0]))
            increment_x -= 450

    if type == "ring":
        for w in range(number):
            ring_group.add(Objects.weapon(
                screenLevelOne.get_rect(), x, y, "Pygame-Haunted-Forest-Game/images/ring.png", 3))


def reset():
    global enemy_hits, FPS, resetV, increment_x, hero_hits, lose
    resetV = True
    enemy_hits = 0
    increment_x = 0
    hero_hits = 0

    lifeHeartGroup.empty()
    ChooseCharacter.hero_group.empty()
    enemies_group.empty()
    enemy_groupReverse.empty()


def restart():
    global resetV, start_game, score, lose

    enemies_group.empty()
    enemy_groupReverse.empty()
    ChooseCharacter.hero_group.empty()
    lifeHeartGroup.empty()
    weapon_group.empty()
    rest_font_group.empty()
    winning_font_Group.empty()
    score = 0
    # print(score)

    makingObjects("enemyRight", number_enemies, x_pos, y_pos)
    makingObjects("enemyLeft", number_enemies, xpos, ypos)
    makingObjects("hearts", number_hearts, heart_pos_x, heart_pos_y)
    #makingObjects("weaponRight", number_hearts,heart_pos_x, heart_pos_y )
    makingObjects("hero", 1, 800, 520)
    lose = False
    resetV = False


def moveEnemy():
    global enemy_hits, enemies_group, score, enemy_hits_right, enemies_left, enemy_hits_left, hero_hits, FPS, enemy_effect
    clock.tick(FPS)

    currentTime = pygame.time.get_ticks()
    if currentTime - start > delay_time:
        enemies_group.draw(screenLevelOne)
        enemy_groupReverse.draw(screenLevelOne)

    for enemy in enemies_group.sprites():
        # for enemy in enemy_groupReverse.sprites():
        for heart in lifeHeartGroup.sprites():

            if pygame.sprite.groupcollide(ChooseCharacter.hero_group, enemies_group, False, True):
                score -= 2
                hero_hits += 1
                heart.kill()
                enemy_effect = pygame.mixer.music.load("Pygame-Haunted-Forest-Game/sound/enemyKill.wav")
                pygame.mixer.music.play(1)

            if enemy_hits_right == 3:

                score += 4
                enemy.kill()
                clock.tick(80)
                enemy_hits_right = 0

    if not lifeHeartGroup and win == False:

        lose_end_Screen()

        reset()

        # lose_end_Screen()

    for enemy in enemy_groupReverse.sprites():
        for heart in lifeHeartGroup.sprites():
            if pygame.sprite.groupcollide(ChooseCharacter.hero_group, enemy_groupReverse, False, True):
                score -= 2
                hero_hits += 1
                heart.kill()
                enemy_effect = pygame.mixer.music.load("Pygame-Haunted-Forest-Game/sound/enemyKill.wav")
                pygame.mixer.music.play(1)

            if enemy_hits_left == 3:

                score += 1
                enemy.kill()
                clock.tick(80)
                enemy_hits_left = 0


def fight():
    global enemy_hits, enemies_group, score, enemy_hits_right, enemies_left, enemy_hits_left, hero_hits, running, theHero
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                weapon_group.add(theHero.throwR(screenRect))
            elif event.key == pygame.K_j:
                weapon_group.add(theHero.throwL(screenRect))
            if event.key == pygame.K_SPACE and resetV == True:
                rest_font_group.empty()
                restart()

    for w in weapon_group.sprites():
        if pygame.sprite.groupcollide(weapon_group, enemies_group, True, False):
            enemy_hits_right += 1
            score += 1
            w.kill()

    for w in weapon_group.sprites():
        if pygame.sprite.groupcollide(weapon_group, enemy_groupReverse, True, False):
            enemy_hits_left += 1
            score += 1
            w.kill()

    for w in weapon_group:
        if w.dir == "right":
            w.rightupdate()
        else:
            w.leftupdate()


# while (running):

#     winning()
#     moveEnemy()
#     fight()
#     renderLevel2()
