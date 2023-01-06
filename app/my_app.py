#  #
import cv2
import pyautogui as pg
from time import sleep
from game_bitcoin import BitcoinGame

pg.FAILSAFE = True
pg.PAUSE = 3
BG = BitcoinGame()
# start_genimotion = (27, 512)
# сollapse_genimotion = (773, 318)
# play_motorola = (795, 673)
# ad_start_window = (962, 918)
# ad_exit = (1151, 116)
# ad_multiplier_2x = (1093, 547)
#
# TAP = [(1149, 723), (1122, 673), (1178, 755)]


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
        sleep(70)
        pg.screenshot('screenshots/start_app.png')
# _____________________________________________________ #

    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    one_loop_clicker()
