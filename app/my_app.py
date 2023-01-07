#  #
import cv2
import pyautogui as pg
from time import sleep
from game_bitcoin import BitcoinGame

pg.FAILSAFE = True
pg.PAUSE = 0.5
BG = BitcoinGame()
images_list = BG.img_coin_list


def search_on_image(img_list: list = images_list):
    for item in img_list:
        path_img_coin = f"/home/rv/Desktop/Cranberry_Branch/app/screenshots/{item}.png"
        btn_list = pg.locateAllOnScreen(path_img_coin)
        sleep(1.5)
        for clc in btn_list:
            pg.doubleClick(clc)


def one_loop_clicker():
    try:
        pg.moveTo(BG.start_genimotion, duration=2)
        pg.click(BG.start_genimotion)
        sleep(5)
        # ________________________________________________________ #
        pg.moveTo(BG.play_motorola, duration=2)
        pg.click(BG.play_motorola)
        sleep(1)
        pg.moveTo(BG.сollapse_genimotion, duration=1)
        pg.click(BG.сollapse_genimotion)
        sleep(90)
        # _______________________________________________________ #
        # path = "/home/rv/Desktop/Cranberry_Branch/app/screenshots/cr_pop.png"
        # ico_cr_pop = path
        pg.moveTo(BG.cr_pop, duration=2)
        pg.click(BG.cr_pop)
        sleep(20)
        # _________________________________________________________ #
        pg.moveTo(BG.cr_pop_new_game, duration=2)
        pg.click(BG.cr_pop_new_game)
        sleep(16)

        point_list = [(697, 458), (755, 458), (813, 458), (871, 458), (929, 458), (987, 458), (1045, 458), (1103, 458),
                 (1161, 458), (1219, 458)]
        for point in point_list:
            pg.moveTo(point, duration=1)
            pg.click(point)
            pg.click(point)
        point_list = [(697, 458+58), (697, 458+58), (697, 458+58), (697, 458+58), (697, 458+58), (697, 458+58), (697, 458+58), (697, 458+58),
                      (697, 458+58), (697, 458+58)]
        for p in point_list[::-1]:
            pg.moveTo(point, duration=1)
            pg.click(point)
            pg.click(point)
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    one_loop_clicker()
