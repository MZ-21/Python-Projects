

import pygame
import Backgrounds
from Objects import weapon
import text
import time
import random
import textWords
import ChooseCharacter
pygame.init()

running = True


# todo list
# Demo: backgrounds, charaters [visuals]
# classes for backgrounds and characters.
# Demo includes showing an explanation of how the game works
# Isra and Midgon: Setup, backgrounds and text
# Ayesha and Kaura: Characters and their details

# week2 to do list;
# demo
# level 1: rocks falling from sky and collection food, also new background
#

# test
# Isra Starts here
clock = pygame.time.Clock()
infoObject = pygame.display.Info()
background_demo = Backgrounds.Backgrounds(
    "Pygame-Haunted-Forest-Game/images/demoBg.png")
# screen= pygame.display.set_mode((background_demo.width+100, background_demo.height+100))


intro_Bg = Backgrounds.Backgrounds(
    "Pygame-Haunted-Forest-Game/images/intro.png")
screen = pygame.display.set_mode(
    (intro_Bg.width+100, intro_Bg.height+100), pygame.RESIZABLE)
print(intro_Bg.width+100)
print(intro_Bg.height+100)

fullscreen = False


# the Textbox in text class takes in the width of the box we are drawing, the height and the rgb color and the x-poistion and y-position
intro_text = text.TextBox(500, 500, "Pygame-Haunted-Forest-Game/images/textBox.png",
                          background_demo.rect.centerx, background_demo.rect.centery)
#demo_box= text.TextBox()
text_group = pygame.sprite.Group()
text_group.add(intro_text)


class GameState:
    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            if not fullscreen:
                screen = pygame.display.set_mode(
                    (event.w, event.h), pygame.RESIZABLE)
            if event.type == pygame.K_f:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode(
                        (screen.get_width(), screen.get_height()))
                else:
                    screen = pygame.display.set_mode(
                        (screen.get_width(), screen.get_height()))

    def __init__(self):
        self.state = 'intro'
        intro_music = pygame.mixer.music.load(
            "Pygame-Haunted-Forest-Game/sound/music.mp3")
        pygame.mixer.music.play(1)

    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'demo'
        render()

    def demo(self):
        pygame.mixer.music.stop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        for h in ChooseCharacter.hero_group.sprites():

            if h.rect.x == 1200-100:
                self.state = 'level1'

        render()

    def lvl1(self):
        import level1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if pygame.sprite.groupcollide(level1.weapon_group, ChooseCharacter.hero_group, True, False):

            self.state = 'level2'

        render()

    def lvl2(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        import level2
        if pygame.sprite.groupcollide(level2.ring_group, ChooseCharacter.hero_group, True, False):

            self.state = "HappyEnding"
        render()

    def Hend(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            #import end

        render()

    def manager(self):
        if self.state == 'intro':
            self.intro()
        if self.state == 'demo':
            self.demo()
        if self.state == 'level1':
            self.lvl1()
        if self.state == "level2":
            self.lvl2()
        if self.state == "HappyEnding":
            self.Hend()

        # isra ends here


demo_font = textWords.Words("Pygame-Haunted-Forest-Game/fonts/block.ttf", 16, background_demo.rect.centerx-250, background_demo.rect.centery -
                            100, "A brave heroine is searching for their long lost loved one.", (0, 0, 0))
font_group = pygame.sprite.Group()  # creating font group
font_group.add(demo_font)  # adding intro_font to font group


intro_font = textWords.Words("Pygame-Haunted-Forest-Game/fonts/block.ttf", 30, screen.get_rect(
).centerx-200, intro_Bg.rect.centery, "HAUNTED FOREST", (0, 0, 0))
Introfont_group = pygame.sprite.Group()  # creating font group
Introfont_group.add(intro_font)


# Initialize Game
def render(*level):
    # clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            pygame.quit()
    if game_state.state == "intro":
        screen.blit(intro_Bg.image, intro_Bg.rect)
        Introfont_group.draw(screen)
        pygame.display.flip()

    if game_state.state == "demo":

        ChooseCharacter.renderTutorial()
        ChooseCharacter.commands()
        screen.fill((0, 0, 0))
        font_group.draw(screen)
        text_group.update()
        # pygame.display.flip()
    if game_state.state == 'level1':
        import level1
        level1.renderLevelOne()
        level1.collideLogic()
        level1.move()
    if game_state.state == "level2":
        import level2
        # level2.makeChar()
        level2.renderLevel2()
        level2.moveEnemy()
        level2.fight()
        level2.winning()
    if game_state.state == "HappyEnding":
        import end
        end.moveWords()
        end.moveHero()
        end.commands()
        end.scrollingFont()
        end.renderEnd()

#     moveHero()
#     commands()
#     scrollingFont()
#     renderEnd()


game_state = GameState()

running = True
while(running):
    game_state.manager()
pygame.quit()
