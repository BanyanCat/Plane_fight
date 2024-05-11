import random
import pygame
from pygame.locals import *
import Plane_Player
from Bullet_Enemy import Bullet_Enemy
from Plane import Plane
from Plane_Player import Plane_Player


'''
实现敌人的显示
'''


class Plane_Enemy(Plane):
    def __init__(self, screen):
        '''
        初始化敌人对象
        :param screen: 主窗体
        '''
        # 初始化飞机信息
        super().__init__(screen,'game_file/plane_enemy.png')
        # 获取对象位置
        self.x = (self.screen.get_width() - self.width) / 2
        self.y = 0
        # 移动方向
        self.direction = 'right'
        pass

    def move(self):
        '''
        敌机移动
        :return:
        '''

        # 左右来回移动
        if self.direction == 'right':
            self.x += 1
            if self.x > self.screen.get_width() - self.width:
                self.direction = 'left'
                pass
            pass
        elif self.direction == 'left':
            self.x -= 1
            if self.x < 0:
                self.direction = 'right'
                pass
            pass
        pass

    def shot(self):

        # 随机射击
        num = random.randint(-10, 10)
        if num == 3:
            newBullet = Bullet_Enemy(self)
            self.bullet_list.append(newBullet)
            pass
        pass

    def attack_hit(self, player):
        '''
        攻击函数
        :param player: 要攻击的对象
        :return:
        '''
        for bullet in self.bullet_list:
            if bullet.y+bullet.height>player.y:
                if bullet.x+bullet.width>player.x and bullet.x<player.x+player.width:
                    # 爆炸效果
                    self.explode(player)
                    pass
            pass
        pass


    pass