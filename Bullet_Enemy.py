import pygame
from pygame.locals import *

from Bullet import Bullet

'''
实现敌方子弹的创建
'''


class Bullet_Enemy(Bullet):
    def __init__(self, enemy):
        '''
        初始化子弹
        :param enemy: 发送子弹的对象
        :param screen: 显示窗体
        '''
        super().__init__(enemy,'game_file/bullet_enemy.png')
        # 子弹所在位置
        self.x = enemy.x + (enemy.width / 2) - (self.width / 2)
        self.y = enemy.y + enemy.height
        pass


    def judge(self):
        '''
        判断子弹是否越界
        :return: True or False表示越界或未越界
        '''
        if self.y > self.screen.get_height():
            return True
        else:
            return False
        pass