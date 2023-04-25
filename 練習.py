import random  # 標準ライブラリ
import sys

import pygame as pg

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    tmr = 0
    bb_img = pg.Surface((20, 20))  # 半径20の正方形
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)  # 赤色で10,10の位置に半径10の円を描く
    bb_img.set_colorkey((0, 0, 0))  # 円の黒い線を消した
    x, y = random.randint(0,1600),random.randint(0,900)  # 縦,横の乱数
    screen.blit(bb_img, [x, y])  #bb_img(赤い円)をぶりっと

    while True:
        for event in pg.event.get():    # これがないとゲームが終わらないから必ず必要
            if event.type == pg.QUIT: 
                return 0

        tmr += 1
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        screen.blit(bb_img, [x, y])  #bb_img(赤い円)をぶりっと.(x,y)でもいい


        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()