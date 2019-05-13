import pygame
from plane_sprites import *

class PlaneGame(object):
    """飞机大战主游戏类"""

    def __init__(self):
        print("初始化游戏中》》》")

        # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)

        # 创建时钟对象
        self.clock = pygame.time.Clock()

        # 创建敌机精灵与精灵组
        self.__creat_sprites()

        # 创建定时器事件——敌机产生
        pygame.time.set_timer(CREAT_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __creat_sprites(self):

        # 创建背景精灵与精灵组
        bg1 = BackgroundSprite()
        bg2 = BackgroundSprite(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄精灵与精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("游戏开始了》》》")

        while True:
            # 1. 设置刷新频率
            self.clock.tick(FRAME_PER_SEC)
            # 2. 事件监听
            self.__event_handler()
            # 3. 碰撞检测
            self.__check_collide()
            # 4. 更新、绘制精灵组
            self.__update_sprites()
            # 5. 更新显示
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREAT_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 1
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -1
        else:
            self.hero.speed = 0

    def __check_collide(self):
        collide_dict =pygame.sprite.groupcollide(self.hero.bullet_group,
                                                 self.enemy_group,
                                                True, True)

        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

        if len(enemies) > 0:
            self.hero.kill()

            PlaneGame.__game_over()

    def __update_sprites(self):

        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束了《《《《》》》》")

        pygame.quit()
        exit()


if __name__ == '__main__':

    game = PlaneGame()

    game.start_game()