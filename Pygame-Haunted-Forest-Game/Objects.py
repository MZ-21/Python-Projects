# this file is created for the game object classes


import pygame
import random
import time


#

clock = pygame.time.Clock()


class GameObject(pygame.sprite.Sprite):

    def __init__(self, x, y, img, speed, screen_rect):
        super().__init__()
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        # self.rect = self.rect.move(speed)
        #self.screen_rect = screen_rect
        self.rect = self.rect.move(speed, 0)


# food, multiplying


class GameItems(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__()
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


Character_image = pygame.image.load(
    "Pygame-Haunted-Forest-Game/images/hero(1).png")
theHero_char = pygame.transform.scale(
    pygame.image.load("Pygame-Haunted-Forest-Game/images/hero(1).png"), (400, 400))


class HeroLevel1(GameObject):
    def __init__(self, screen_rect, image):
        self.speed = 4
        self.screen_rect = screen_rect
        self.image = image
        self.setValue = 0
        self.rand_x = 400
        self.rand_y = 400
        self.string = image
        super().__init__(self.rand_x, self.rand_y, self.image, self.speed, self.screen_rect)
        self.jumppos = 0

    def jump(self, dir):
        self.dir = dir
        if self.dir == "up":
            self.rect.y += 10
            self.jumppos = 1
        elif self.dir == "down":
            self.rect.y -= 10
            self.jumppos = 0

    def left(self):
        self.rect = self.rect.move(-5, 0)

    def right(self):
        self.rect = self.rect.move(5, 0)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            if self.rect.x < 0:
                self.rect.x = 0
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            if self.rect.x > self.screen_rect.width-75:
                self.rect.x = self.screen_rect.width-75
        elif keys[pygame.K_DOWN]:
            self.jump('up')
            if self.rect.y > self.screen_rect.height-100:
                self.rect.y = self.screen_rect.height-100
        elif keys[pygame.K_UP]:
            self.jump('down')
            if self.rect.y < 0:
                self.rect.y = 0


class Hero(GameObject):
    def __init__(self, screen_rect, img_path):
        # rand_x = random.randint(0, screen_rect.width)
        # rand_y = random.randint(0, screen_rect.height)
        self.speed = 5
        rand_x = 800
        rand_y = 520  # will spawn on the ground
        self.string = img_path
        #super().__init__(rand_x, rand_y, "hiker.png", [8, 8],screen_rect)
        self.image = img_path
        super().__init__(rand_x, rand_y, self.image, self.speed, screen_rect)
        self.jumppos = 0
        self.gravity = 0.6
        self.jump_height = 20
        self.velocity = self.jump_height
        self.jumping = False

    def jump(self, dir):
        self.dir = dir
        if self.dir == "up":
            # self.rect.y += 50
            # time.sleep(0.05)
            self.rect.y -= 60
            self.jumppos = 1
        elif self.dir == "down":
            self.rect.y += 60
            self.jumppos = 0

    def throwR(self, screen_rect):
        weapon = WeaponRock(
            self.rect.x+100, self.rect.y+23, "Pygame-Haunted-Forest-Game/images/one-rock-1.png", 32, screen_rect)
        weapon.dir = "right"
        return weapon

    def throwL(self, screen_rect):
        weapon = WeaponRock(
            self.rect.x+100, self.rect.y+23, "Pygame-Haunted-Forest-Game/images/one-rock-1.png", 32, screen_rect)
        weapon.dir = "left"
        return weapon

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        # elif keys[pygame.K_DOWN]:
        #     self.jump('down')
        elif keys[pygame.K_UP]:
            self.jump('up')
        clock.tick(90)


class AnimationSprite(pygame.sprite.Sprite):
    def __init__(self, position, images):
        super().__init__(AnimationSprite, self)

        size = (15, 15)
        self.rect = pygame.Rect(position, size)
        self.images = images
        self.images_right = images
        self.images_left = [pygame.transform.flip(images, True, False)]
        self.index = 0
        self.image = images[self.index]

        self.jump("down")
        self.rect.y -= self.speed
        self.rect.y += self.speed

        self.aniamtion_frames = 6
        self.current_frame = 0

    def update_time_dependent(self, dt):
        # Will update the images every 0.1 second
        # dt = time elapsed between each frame

        if self.velocity.x > 0:
            self.images = self.images_right
        elif self.velocity.x < 0:
            self.images = self.images_left


class WeaponRock(pygame.sprite.Sprite):
    # what class should look like
    def __init__(self, x, y, img, speed, screen_rect):
        super().__init__()
        rock_image = pygame.image.load(
            "Pygame-Haunted-Forest-Game/images/one-rock-1.png")
        self.image = pygame.transform.scale(
            rock_image, (rock_image.get_width()*0.02, rock_image.get_height()*0.02))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed
        self.dir = "default"

    def rightupdate(self):
        self.rect.x += self.speed

    def leftupdate(self):
        self.rect.x -= self.speed


class TextBox(pygame.sprite.Sprite):
    def __init__(self, width, height, colour, pos_x, pos_y):
        # calling parent class constructor of sprite
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(colour)  # changing the colour
        # getting the rectangle object of the image
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]


class GameDynamicObjects(pygame.sprite.Sprite):
    def __init__(self, x, y, img_path, screen_rect):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.screen_rect = screen_rect


class Rocks(GameDynamicObjects):
    def __init__(self, screen_rect, x, y):
        rand_x = random.randint(10, screen_rect.width)
        rand_y = random.randint(y, 10)
        self.x = rand_x
        self.y = rand_y
        self.speed = 6
        super().__init__(self.x, self.y, "Pygame-Haunted-Forest-Game/images/rock.png", screen_rect)

    def update(self):
        self.rect = self.rect.move(0, self.speed)


class Food(GameDynamicObjects):

    def __init__(self, screen_rect, x, y):
        rand_x = random.randint(x, screen_rect.right - x)
        rand_y = random.randint(y, 10)
        self.x = rand_x
        self.value = 0
        self.y = rand_y
        # self.dir = dir
        self.speed = 3
        super().__init__(self.x, self.y, "Pygame-Haunted-Forest-Game/images/coin.png", screen_rect)

    def update(self):
        self.rect = self.rect.move(0, self.speed)
        if (self.rect.bottom >= self.screen_rect.height - 100):
            self.value = 1
            self.speed = -self.speed

        if self.value == 1:
            if (self.rect.y < 400):
                self.speed = -self.speed


class weapon(GameDynamicObjects):
    def __init__(self, screen_rect, x, y, image_path, speed):
        rand_x = random.randint(x, screen_rect.right - x)
        rand_y = random.randint(y, 10)
        self.x = rand_x
        self.value = 0
        self.y = rand_y
        # self.dir = dir
        self.speed = speed
        super().__init__(self.x, self.y, image_path, screen_rect)

    def update(self, height_boundary, width_boundary):
        self.rect = self.rect.move(0, self.speed)
        if (self.rect.bottom >= self.screen_rect.height - (height_boundary)):
            self.value = 1
            self.speed = -self.speed

        if self.value == 1:
            if (self.rect.y < width_boundary):
                self.speed = -self.speed


class enemyAnimation(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()

        self.images = []

        enemy1 = pygame.image.load(
            "Pygame-Haunted-Forest-Game/images/enemy1.png")
        enemy1_image = pygame.transform.scale(
            enemy1, (enemy1.get_width()*0.25, enemy1.get_height()*0.25))

        enemy2 = pygame.image.load(
            "Pygame-Haunted-Forest-Game/images/enemy2.png")
        enemy2_image = pygame.transform.scale(
            enemy2, (enemy2.get_width()*0.25, enemy2.get_height()*0.25))

        enemy3 = pygame.image.load(
            "Pygame-Haunted-Forest-Game/images/enemy3.png")
        enemy3_image = pygame.transform.scale(
            enemy3, (enemy3.get_width()*0.25, enemy3.get_height()*0.25))

        enemy3_img = pygame.transform.flip(enemy3_image, True, False)
        enemy2_img = pygame.transform.flip(enemy2_image, True, False)
        enemy1_img = pygame.transform.flip(enemy1_image, True, False)

        self.images.append(enemy1_img)
        self.images.append(enemy2_img)
        self.images.append(enemy3_img)

        # self.x = x
        # self.y = y

        self.rect = enemy1_image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.speed = speed

        self.current_frame = 0

        self.image = self.images[0]
        super().__init__()

    def update(self, screen):
        variable_Frame = 6
        # self.current_frame += 1

        # for self.current_frame in range(2):

        if self.current_frame >= len(self.images) * variable_Frame:
            self.current_frame = 0
            self.rect.y = self.rect.y - 49

        if self.current_frame % variable_Frame == 0:
            if self.current_frame//variable_Frame == 1:
                self.rect.y = self.rect.y + 33
            elif self.current_frame//variable_Frame == 2:
                self.rect.y = self.rect.y + 16

        self.image = self.images[self.current_frame//variable_Frame]
        self.current_frame += 1
        self.rect = self.rect.move(self.speed)

        if self.rect.x < screen.get_rect().x:
            print(screen.get_rect().x)
            self.rect.x = random.randint(1090, 1250)

        self.rect = self.rect.move(self.speed)


class enemyAnimationReverse(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()

        self.images = []

        enemy1 = pygame.image.load(
            "Pygame-Haunted-Forest-Game/images/enemy1.png")
        enemy1_image = pygame.transform.scale(
            enemy1, (enemy1.get_width()*0.25, enemy1.get_height()*0.25))

        enemy2 = pygame.image.load(
            "Pygame-Haunted-Forest-Game/images/enemy2.png")
        enemy2_image = pygame.transform.scale(
            enemy2, (enemy2.get_width()*0.25, enemy2.get_height()*0.25))

        enemy3 = pygame.image.load(
            "Pygame-Haunted-Forest-Game/images/enemy3.png")
        enemy3_image = pygame.transform.scale(
            enemy3, (enemy3.get_width()*0.25, enemy3.get_height()*0.25))

        self.images.append(enemy1_image)
        self.images.append(enemy2_image)
        self.images.append(enemy3_image)

        # self.x = x
        # self.y = y

        self.rect = enemy1_image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.speed = speed

        self.current_frame = 0

        self.image = self.images[0]
        super().__init__()

    def update(self, screen):
        variable_Frame = 6
        # self.current_frame += 1

        # for self.current_frame in range(2):

        if self.current_frame >= len(self.images) * variable_Frame:
            self.current_frame = 0
            self.rect.y = self.rect.y - 49

        if self.current_frame % variable_Frame == 0:
            if self.current_frame//variable_Frame == 1:
                self.rect.y = self.rect.y + 33
            elif self.current_frame//variable_Frame == 2:
                self.rect.y = self.rect.y + 16

        self.image = self.images[self.current_frame//variable_Frame]
        self.current_frame += 1
        self.rect = self.rect.move(self.speed)

        if self.rect.x > screen.get_rect().width:
            # print(screen.get_rect().x)
            self.rect.x = random.randint(0, 100)

        self.rect = self.rect.move(self.speed)
