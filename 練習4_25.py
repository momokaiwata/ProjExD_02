import random
import sys

import pygame as pg


delta = {
        pg.K_UP: (0, -1), # 移動量の値であり、(横,縦)
        pg.K_DOWN: (0, +1),
        pg.K_LEFT: (-1, 0),
        pg.K_RIGHT: (+1, 0),
        }


def check_bound(scr_rect : pg.Rect, obj_rect : pg.Rect) -> tuple[bool, bool]:
    """
    オブジェクトが画面内 or 画面外を判定し、真理値タプルを返す関数
    引数1 : 画面SurfaceのRect
    引数1 : こうかとん　または　爆弾SurfaceのRect
    戻り値 : 横方向　縦方向のはみ出し判定結果 (画面内：True/画面外：False)
    """
    yoko, tate = True, True
    if obj_rect.left < scr_rect.left or scr_rect.right < obj_rect.right:
        yoko = False
    if obj_rect.top < scr_rect.top or scr_rect.bottom < obj_rect.bottom:
        tate = False
    return yoko, tate 



def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rect = kk_img.get_rect() # ??
    kk_rect.center = 900, 400

    bb_img = pg.Surface((20, 20))  # 半径20の正方形
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)  # 赤色で10,10の位置に半径10の円を描く
    bb_img.set_colorkey((0, 0, 0))  # 円の黒い線を消した
    x, y = random.randint(0,1600),random.randint(0,900)  # 縦,横の乱数
    screen.blit(bb_img, [x, y])  #bb_img(赤い円)をぶりっと
    vx, vy = +1, +1 #横、縦速度
    bb_rect = bb_img.get_rect() # ?? 
    bb_rect.center = x, y # 爆弾の中心座標に x, y を ?
    tmr = 0

    while True:
        for event in pg.event.get():    #これがないとゲームが終わらないから必ず必要
            if event.type == pg.QUIT: 
                return 0

        tmr += 1

        key_list = pg.key.get_pressed()
        for k, mv in delta.items(): # mv = 移動量
            if key_list[k]:
                kk_rect.move_ip((mv))

        if check_bound(screen.get_rect(), kk_rect) != (True, True):
            for k, mv in delta.items(): # mv = 移動量
                if key_list[k]:
                    kk_rect.move_ip(-mv[0], -mv[1])

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rect)
        bb_rect.move_ip(vx, vy) #移動部分
        yoko, tate = check_bound(screen.get_rect(), bb_rect)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1

        screen.blit(bb_img, bb_rect) #表示
        # screen.blit(bb_img, [x, y])  #bb_img(赤い円)をぶりっと

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()