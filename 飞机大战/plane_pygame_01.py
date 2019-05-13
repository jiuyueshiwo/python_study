import pygame
from plane_sprites import *

pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
background = pygame.image.load("./images/background.png")
screen.blit(background,(0, 0))

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero,(200, 500))

# 更新显示之前所有绘制的图像
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

hero_rect = pygame.Rect(200, 500, 102, 126)

#创建敌机精灵与精灵组
enemy01 = GameSprite("./images/enemy1.png")
enemy02 = GameSprite("./images/enemy1.png", 2)
enemy03 = GameSprite("./images/enemy1.png", 3)
enemy_group = pygame.sprite.Group(enemy01, enemy02, enemy03)


# 游戏循环
while True:

    # 可以指定循环体内部代码执行频率
    clock.tick(60)

    # 事件监听
    for event in pygame.event.get():

        # 判断事件是否是退出
        if event.type == pygame.QUIT:
            print("退出游戏》》》》》")

            pygame.quit()
            exit()

    event_list = pygame.event.get()
    if len(event_list) > 0:
        print(event_list)

    hero_rect.y -= 1

    if hero_rect.y <= -126:
        hero_rect.y = 700

    screen.blit(background, (0, 0))
    screen.blit(hero, hero_rect)

    #让精灵组调用update和draw方法
    enemy_group.update()

    enemy_group.draw(screen)

    pygame.display.update()



pygame.quit()