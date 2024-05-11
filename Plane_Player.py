import pygame
from pygame.locals import *

from Bullet_Player import Bullet_Player
from Plane import Plane

'''
实现飞机的显示，并且可以控制飞机的移动【面向对象】
'''


class Plane_Player(Plane):
    def __init__(self, screen):
        '''
        初始化函数
        :param screen: 主窗体对象
        '''
        # 初始化飞机信息
        super().__init__(screen,'game_file/plane_player.png')
        # 飞机的默认位置
        self.x = (self.screen.get_width() - self.width) / 2
        self.y = self.screen.get_height() - self.height
        pass

    def move_left(self):
        '''
        左移动
        :return:
        '''
        if self.x > 0:
            self.x -= 10
            pass
        pass

    def move_right(self):
        '''
        左移动
        :return:
        '''
        if self.x < self.screen.get_width() - self.image.get_width():
            self.x += 10
            pass
        pass



    def shot(self):
        newBullet = Bullet_Player(self)
        self.bullet_list.append(newBullet)
        pass

    def attack_hit(self,enemy):
        '''
        攻击函数
        :param enemy: 要攻击的对象
        :return:
        '''
        for bullet in self.bullet_list:
            if bullet.y<enemy.y+enemy.height:
                if bullet.x+bullet.width>enemy.x and bullet.x<enemy.x+enemy.width:
                    # 爆炸效果
                    self.explode(enemy)
                    pass
            pass
        pass

    pass