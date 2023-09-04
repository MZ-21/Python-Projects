
import Objects
import textWords
import pygame
print("importing pygame")
print("textWors & objects 1")


pygame.init()
print("init")

running = True

#level1BackGround = Backgrounds.Backgrounds("level1.png")
screen = pygame.display.set_mode(  # screen dimensions
    (1200, 700))  # pygame.resizable


screenW = 1200
screenH = 700
# screen= pygame.display.set_mode((screenW, screenH))
food_Group = pygame.sprite.Group()
rock_group = pygame.sprite.Group()
lifeHeartGroup = pygame.sprite.Group()
hero_Group = pygame.sprite.Group()

timer = pygame.time.Clock()
counter = 0
speeds = 3
done = False


chooseCharText = textWords.Words("Pygame-Haunted-Forest-Game/fonts/block.ttf",
                                 25, screenW/4, screenH/6, "CHOOSE A CHARACTER", (255, 255, 255))
textGroup = pygame.sprite.Group()
textGroup.add(chooseCharText)
textBox_group = pygame.sprite.Group()

# scrolling text
# scrollingText_group = pygame.sprite.Group()
# scrollingText_group.add(textWords.Words("block.ttf",12,screen.get_width()/2,screen.get_height()-100,"",(255,255,255)))
hiker_img = "Pygame-Haunted-Forest-Game/images/hiker.png"
brett_img = "Pygame-Haunted-Forest-Game/images/hero(1).png"


hero1 = Objects.HeroLevel1(screen.get_rect(), hiker_img)
hero1.rect.x = screenW/4

hero2 = Objects.HeroLevel1(screen.get_rect(), brett_img)
hero2.rect.x = screenW/2

hero_group = pygame.sprite.Group()

font = pygame.font.Font("Pygame-Haunted-Forest-Game/fonts/block.ttf", 10)

messagesR2 = ["F o l l o w  t h e  i n s t r u c t i o n s  t o  p r o c e e d  t o  t h e  g a m e.  P r e s s  E n t e r  ", "M o v e  l e f t  o r  r i g h t  u s i n g  t h e  a r r o w  k e y s ",
              "M o v e  u p  o r  d o w n  u s i n g  t h e  a r r o w  k e y s ", "P r o c e e d  t o  t h e  r i g h t  s i d e  o f  t h e  s c r e e n  t o  m o v e  t o  t h e  g a m e "]
active_msg = 0
#message = messagesR1[active_msg]
message2 = messagesR2[active_msg]

nextScene = False

snip = font.render('', True, 'white')
snip2 = font.render('', True, 'white')
arrow_group = pygame.sprite.Group()
# arrow_image = pygame.image.load("arrow1.png")
# arrow_rect = arrow_image.get_rect()
doneWC = False

hero_group.add(hero1, hero2)


def scrollingFont():
    global counter, done, nextScene, snip, snip2

    if counter < speeds*len(message2):
        counter += 1
    elif counter >= speeds:
        done = True

    pygame.init()
    # snip = font.render(message[0:counter//speeds],True,'white')
    snip2 = font.render(message2[0:counter//speeds], True, 'white')


value = False


def renderTutorial():

    textGroup.draw(screen)
    textGroup.update()

    hero_group.draw(screen)
    hero_group.update()

    textBox_group.draw(screen)
    textBox_group.update()

    # global timer, nextScene
    global nextScene, snip, snip2

    if(nextScene == True):
        textGroup.add(textWords.Words("Pygame-Haunted-Forest-Game/fonts/block.ttf", 25, screenW /
                      3, screenH/10, "TUTORIAL", (255, 255, 255)))
        #

    screen.blit(snip, (10, screen.get_height()-50))
    screen.blit(snip2, (10, screen.get_height()-30))

    # arrow_group.draw(screen)
    # arrow_group.update()
    rock_group.draw(screen)
    rock_group.update()

    if nextScene == True:
        scrollingFont()

    pygame.display.flip()


# renderTutorial()

# running flag
running = True
# Creating game while loop


def commands():
    global done, nextScene, message2, counter, active_msg, doneWC
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for character in hero_group.sprites():
                if character.rect.collidepoint(event.pos):

                    hero_group.empty()
                    # image = pygame.transform.scale(character.image,(100,186))
                    # character.image = image
                    character.rect.x = screenW/2
                    # print(character.selectedImage)
                    hero_group.add(character)
                    textGroup.empty()
                    nextScene = True
                    active_msg = 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and done and active_msg == 1:

                message2 = messagesR2[1]
                done = False
                counter = 0
                active_msg += 1
                print(active_msg)

            elif event.key == pygame.K_LEFT and done and active_msg == 2:
                done = False

                message2 = messagesR2[2]
                # message2 = messagesR2[active_msg]
                print(active_msg)
                active_msg += 1
                counter = 0
            elif event.key == pygame.K_RIGHT and done and active_msg == 2:
                done = False
                message2 = messagesR2[2]
                # message2 = messagesR2[active_msg]
                counter = 0
                active_msg += 1
            elif event.key == pygame.K_UP and done and active_msg == 3:
                done = False
                message2 = messagesR2[3]
                counter = 0
                active_msg += 1
            elif event.key == pygame.K_DOWN and done and active_msg == 3:
                done = False
                message2 = messagesR2[3]
                counter = 0
                active_msg += 1
                doneWC = True


# while(running):

#     screen.fill((0,0,0))
#     commands()
#     renderTutorial()


# pygame.quit()
