
import pyautogui as pg

pg.PAUSE = 1.5

y = 458
list_X = [697, 755, 813, 871, 929, 987, 1045, 1103, 1161, 1219]
# point_list = [(697, 458), (755, 458), (813, 458), (871, 458), (929, 458), (987, 458), (1045, 458), (1103, 458), (1161, 458)]
for j in range(10):
    for cur in list_X:
        x = cur
        point = (x, y)
        pg.moveTo(point, duration=1.5)
        pg.click(point)
        pg.click(point)
    y += 58
    print()

