import pygame


'''
实现玩家子弹的创建
'''


class Bullet(object):
    def __init__(self, plane, imageName):
        '''
        初始化子弹
        :param plane: 发送子弹的对象
        :param screen: 显示窗体
        '''

        self.image = pygame.image.load(imageName)
        self.screen = plane.screen
        # 子弹宽高
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        pass

    def display(self):
        '''
        显示子弹
        :return:
        '''
        self.screen.blit(self.image, (self.x, self.y))
        pass

    def move(self):
        '''
        移动子弹
        :return:
        '''

        if str(type(self)) == "<class 'Bullet_Player.Bullet_Player'>":
            self.y -= 5
        else:
            self.y += 5
            pass
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
