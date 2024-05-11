import pygame
import Key_Control
from Key_Control import Key_Control
import Plane_Player
from Plane_Enemy import Plane_Enemy
from Plane_Player import Plane_Player


def main():
    '''
    Main function
    游戏入口
    :return:
    '''
    # 创建游戏窗口
    screen = pygame.display.set_mode((350, 500), depth=32)
    # 设置游戏背景
    background = pygame.image.load('game_file/bg_space.png')
    pygame.display.set_caption("飞机小游戏")

    # 添加背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load('game_file/bg_music.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)  # 循环次数 -1表示无限循环

    # 创建玩家飞机对象
    player = Plane_Player(screen)
    enemy = Plane_Enemy(screen)

    pygame.init()

    font = pygame.font.Font(None, 40)
    you_win = font.render('YOU WIN! ', 1, (0, 0, 255))
    you_lost = font.render('YOU LOST! ', 1, (255, 0, 0))

    run=True

    # 设定要显示的内容
    while (True):
        screen.blit(background, (0, 0))
        # 显示玩家飞机图片
        player.display()

        # 显示敌人、敌机移动、随机射击
        enemy.display()
        enemy.move()
        enemy.shot()

        # 获取键盘事件
        Key_Control.key_control(player)

        # 玩家与敌机互相击中检测
        player.attack_hit(enemy)
        enemy.attack_hit(player)

        # 敌人消灭，结束


        # 更新显示内容
        if run:
            if enemy.life <= 0:
                screen.blit(you_win, (100, 230))
                run=False

        # 主角被打死，结束
            if player.life <= 0:
                screen.blit(you_lost, (100, 230))
                run=False
            pygame.display.update()
        else:
            pygame.mixer.music.pause()

        # 控制窗体刷新频率：n次/每秒
        pygame.time.Clock().tick(60)
        pass
    pass


if __name__ == '__main__':
    main()
