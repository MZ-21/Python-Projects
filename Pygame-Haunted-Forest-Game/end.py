import Backgrounds
import pygame
import textWords
import time
import ChooseCharacter
import Objects

pygame.init()

castleBackground = Backgrounds.Backgrounds(
    "Pygame-Haunted-Forest-Game/images/castle.jpg")


# screen image and rect
screen = pygame.display.set_mode(
    (castleBackground.width, castleBackground.height))
screen_rect = screen.get_rect()

#text and text_Group
text = textWords.Words("Pygame-Haunted-Forest-Game/fonts/end.ttf", 60, screen_rect.width /
                       4+10, 50, "TH E  END", (0, 0, 0))
text_Group = pygame.sprite.Group()
text_Group.add(text)
textSpeed = 5
textSpeed_y = 0

# scrolling text
messagesR2 = ["M y  L O V E", "I  f o u n d  y o u  ", " "]
active_msg = 0
message2 = messagesR2[active_msg]

font = pygame.font.Font("Pygame-Haunted-Forest-Game/fonts/block.ttf", 8)
snip = font.render('', True, 'black')


counter = 0
speeds = 3
done = False
done2 = False
text1Finished = False
NextScene = False

for heroes in ChooseCharacter.hero_group.sprites():
    if(heroes.string == "Pygame-Haunted-Forest-Game/images/hiker.png"):

        theHero2 = Objects.Hero(
            screen_rect, "Pygame-Haunted-Forest-Game/images/hiker.png")

        ChooseCharacter.hero_group.empty()
        ChooseCharacter.hero_group.add(theHero2)

    if heroes.string == "Pygame-Haunted-Forest-Game/images/hero(1).png":
        theHero2 = Objects.Hero(
            screen_rect, "Pygame-Haunted-Forest-Game/images/hero(1).png")

        ChooseCharacter.hero_group.empty()
        ChooseCharacter.hero_group.add(theHero2)


def scrollingFont():
    global counter, done, snip, snip2, counter2, done2, text1Finished

    if counter < speeds*len(message2):
        counter += 1
    elif counter >= speeds:
        done = True
        text1Finished

    snip2 = font.render(message2[0:counter//speeds], True, 'black')


def commands():
    global done, message2, counter, active_msg,  counter2, done2, active_msg2, text1Finished
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # if event.type == pygame.KEYDOWN:
        if event.type == pygame.KEYDOWN and done and len(message2)-1:
            print("in comannnnds")
            message2 = messagesR2[active_msg+1]
            done = False
            counter = 0
            active_msg += 1


# hero properties
hero_speed_x = 10
hero_speed_y = -2
hero_width = 65
hero_height = 137
hero_increase = 1

# clock
clock = pygame.time.Clock()


# princess image and rect and positions
princess = pygame.image.load("Pygame-Haunted-Forest-Game/images/princess.png")
princess_rect = princess.get_rect()
shift_x_of_princess = 450
shift_y_of_princess = 100
princess_rect.x = screen_rect.width-450
princess_rect.y = screen_rect.height-250

# HERO IMAGE
for hero in ChooseCharacter.hero_group.sprites():
    hero.rect.x = 0
    hero.rect.y = screen_rect.height-150


def moveWords():
    global textSpeed, textSpeed_y, text
    text.rect = text.rect.move(float(textSpeed), textSpeed_y)

    if text.rect.x > screen_rect.width/4 + 200:
        textSpeed = -textSpeed

    if text.rect.x < screen_rect.width/4:
        textSpeed = -textSpeed

    if done == True and len(message2)-1 == 0 and text.rect.x == screen_rect.width/2.5:
        textSpeed = 0
        textSpeed_y = 5

    if text.rect.y == screen_rect.height/2:
        textSpeed_y = 0
        text2 = textWords.Words(
            "Pygame-Haunted-Forest-Game/fonts/end.ttf", 150, text.rect.x-200, screen_rect.height/3, "TH E  END", (0, 0, 0))
        text_Group.empty()
        text_Group.add(text2)
    time.sleep(0.05)


def moveHero():
    global hero_speed_x, hero_speed_y
    for hero in ChooseCharacter.hero_group.sprites():
        hero.rect = hero.rect.move(hero_speed_x, hero_speed_y)

        if hero.rect.x == princess_rect.x-100:
            hero_speed_x = 0
        if hero.rect.y == princess_rect.y:
            hero_speed_y = 0

    shrink()


def shrink():
    global hero_increase
    for hero in ChooseCharacter.hero_group.sprites():
        if hero_speed_x != 0 and hero_speed_y != 0:
            hero.image = pygame.transform.scale(
                hero.image, (hero_width-hero_increase, hero_height-hero_increase))
            hero_increase += 0.06


def renderEnd():
    # blitting screen
    screen.blit(castleBackground.image, castleBackground.rect)

    # blitting words
    text_Group.draw(screen)
    text_Group.update()

    # blitting princess
    screen.blit(princess, princess_rect)

    # blitting hero
    ChooseCharacter.hero_group.draw(screen)
    ChooseCharacter.hero_group.update()

    # blitting convo
    if hero_speed_x == 0 and hero_speed_y == 0:
        screen.blit(snip, (princess_rect.x, princess_rect.y-20))

        for hero in ChooseCharacter.hero_group.sprites():
            screen.blit(snip2, (hero.rect.x-20, hero.rect.y-10))

    pygame.display.flip()


running = True

# while(running):
#     moveWords()
#     moveHero()
#     commands()
#     scrollingFont()
#     renderEnd()
#     time.sleep(0.05)
# pygame.quit()
