import pygame


class Plane():
    def __init__(self, screen, imageName):
        '''
        父类飞机初始化
        :param screen: 主窗体
        :param imageName: 对象图形地址
        '''
        # 设置要显示内容的窗口
        self.screen = screen
        # 生成飞机的图片对象
        self.image = pygame.image.load(imageName)
        # 飞机的宽高
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        # 子弹列表
        self.bullet_list = []
        # 生命值
        self.life = 100
        pass

    def explode(self, plane):
        '''
        爆炸效果
        :param plane:
        :return:
        '''
        imageName = 'game_file/bump.png'
        image = pygame.image.load(imageName)
        plane.screen.blit(image, (
            plane.x + plane.width / 2 - image.get_width() / 2, plane.y + plane.height / 2 - image.get_height() / 2))
        if plane.life > 0:
            plane.life -= 1
        pass

    def display(self):
        '''
        在主窗口中显示飞机以及射击子弹
        :return:
        '''
        self.screen.blit(self.image, (self.x, self.y))

        # 血条(头顶的绿色背景矩形）
        pygame.draw.rect(self.screen, (0, 128, 0), (self.x, self.y, 40, 8))
        # 血条(头顶的红色背景矩形，即：消耗的血）
        pygame.draw.rect(self.screen, (255, 0, 0), (self.x + self.life * 0.4, self.y, 40 - self.life * 0.4, 8))

        del_bullet_list = []
        for bullet in self.bullet_list:
            if bullet.judge():
                del_bullet_list.append(bullet)
                pass
            pass
        for bullet in del_bullet_list:
            self.bullet_list.remove(bullet)
            pass
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
        pass

    pass
