import random
import pygame

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
FRAME_PER_SEC = 60
CREAT_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, imagename, speed=1):

        # 调用父类的初试化方法
        super().__init__()

        # 定义对象属性
        self.image = pygame.image.load(imagename)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):

        self.rect.y += self.speed


class BackgroundSprite(GameSprite):
    """游戏背景精灵类"""
    def __init__(self, is_alt=False):

        super().__init__("./images/background.png")

        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):

        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵类"""

    def __init__(self):

        super().__init__("./images/enemy1.png")

        self.speed = random.randint(1, 3)

        self.rect.bottom = 0

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):

        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            self.kill()


class Hero(GameSprite):

    def __init__(self):

        super().__init__("./images/me1.png", 0)

        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 创建子弹精灵组
        self.bullet_group = pygame.sprite.Group()

    def update(self):

        self.rect.x += self.speed

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.width:
            self.rect.right = SCREEN_RECT.width

    def fire(self):

        for i in (0, 1, 2):

            bullet = Bullet()

            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx

            self.bullet_group.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):

        super().__init__("./images/bullet1.png", -2)

    def update(self):

        super().update()

        if self.rect.bottom < 0:
            self.kill()



