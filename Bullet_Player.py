import pygame

from Bullet import Bullet

'''
实现玩家子弹的创建
'''


class Bullet_Player(Bullet):
    def __init__(self, player):
        '''
        初始化子弹
        :param player: 发送子弹的对象
        :param screen: 显示窗体
        '''
        super().__init__(player,'game_file/bullet_player.png')
        # 子弹所在位置
        self.x = player.x + (player.width / 2) - (self.width / 2)
        self.y = player.y - self.height
        pass

    def judge(self):
        '''
        判断子弹是否越界
        :return: True or False表示越界或未越界
        '''
        if self.y < 0:
            return True
        else:
            return False
        pass

