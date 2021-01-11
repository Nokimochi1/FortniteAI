import numpy as np
import cv2 as cv

def graph():
    img = cv.imread("FortniteBot/screenshots/fortnitemap.png", cv.IMREAD_COLOR)
    start = cv.imread("FortniteBot/pictures/startpoint.png", cv.IMREAD_COLOR)
    cords_list = []


    result = cv.matchTemplate(img, start, cv.TM_CCOEFF_NORMED)


    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)


    start_point = max_loc

    threshold = max_val




    end_points = []
    end_dots = []


    for x in range(1, 5):
        end = cv.imread(f"FortniteBot/pictures/endpoint{x}.png", cv.IMREAD_COLOR)
        endCords = cv.matchTemplate(img, end, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(endCords)


        threshold = 0.87
        if max_val >= threshold:


            end_point = max_loc
            end_points.append(end_point)

    for x in range(10, 620, 16):
        for y in range(10, 660, 16):
            cv.circle(img, (y, x), 4, (0, 0, 255), -1)
            cords_list.append((x, y))

    for elem in end_points:
        end_dot = min(cords_list, key=lambda c: (c[0]- elem[0])**2 + (c[1]- elem[1])**2)
        end_dots.append(end_dot)

    start_dot = min(cords_list, key=lambda c: (c[0]- start_point[0])**2 + (c[1]- start_point[1])**2)

    return cords_list, end_dots, start_dot

