import sys

import pygame
from pygame.locals import *

'''
检测键盘事件
'''

class Key_Control(object):
    def __init__(self):
        pass
    @classmethod
    def key_control(cls,player_obj):
        '''
        定义普通的函数，用来实现键盘的检测
        :param player_obj: 可控制检测的对象
        :return:
        '''
        # 获取键盘事件
        eventlist = pygame.event.get()
        for event in eventlist:
            if event.type == QUIT:
                print("退出")
                sys.exit()
                pass
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    print("left")
                    player_obj.move_left()  # 调用对象左移函数
                    pass
                elif event.key == K_d or event.key == K_RIGHT:
                    print("right")
                    player_obj.move_right()  # 调用对象右移函数
                    pass
                elif event.key == K_SPACE:
                    print("space")
                    player_obj.shot()  # 按空格键射击
                    pass
                pass
            pass
        pass
