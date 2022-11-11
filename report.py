#copyright (c) 2019
#jodathecoda@yahoo.com

import os
from math import*
import time
from time import strftime
import random
import settings

graph = {'pos1': [1, 0],
         'pos2': [2, 0],
         'pos3': [3, 0],
         'pos4': [4, 0],
         'pos5': [5, 0],
         'pos6': [6, 0],
         'pos7': [7, 0],
         'pos8': [8, 0],
         'pos9': [9, 0],
         'pos10': [10, 0],
         'pos11': [11, 0],
         'pos12': [12, 0],
         'pos13': [13, 0],
         'pos14': [14, 0],
         'pos15': [15, 0],
         'pos16': [16, 0],
         'pos17': [17, 0],
         'pos18': [18, 0],
         'pos19': [19, 0],
         'pos20': [20, 0],
         'pos21': [21, 0],
         'pos22': [22, 0],
         'pos23': [23, 0],
         'pos24': [24, 0],
         'pos25': [25, 0],
         'pos26': [26, 0],
         'pos27': [27, 0],
         'pos28': [28, 0],
         'pos29': [29, 0],
         'pos30': [30, 0],
         'pos31': [31, 0],
         'pos32': [32, 0],
         'pos33': [33, 0],
         'pos34': [34, 0],
         'pos35': [35, 0],
         'pos36': [36, 0],
         'pos37': [37, 0],
         'pos38': [38, 0],
         'pos39': [39, 0],
         'pos40': [40, 0],
         'pos41': [41, 0],
         'pos42': [42, 0],
         'pos43': [43, 0],
         'pos44': [44, 0],
         'pos45': [45, 0],
         'pos46': [46, 0],
         'pos47': [47, 0],
         'pos48': [48, 0],
         'pos49': [49, 0],
         'pos50': [50, 0],
         'pos51': [51, 0],
         'pos52': [52, 0],
         'pos53': [53, 0],
         'pos54': [54, 0]}

HEIGHT = 10
WIDTH = 50
MARKER = '.'
FILL_CHARACTER = ' '

external_list = []

def run(datalist):
    l = graph.get('pos1')
    l[1] = datalist[0]
    l = graph.get('pos2')
    l[1] = datalist[1]
    l = graph.get('pos3')
    l[1] = datalist[2]
    l = graph.get('pos4')
    l[1] = datalist[3]
    l = graph.get('pos5')
    l[1] = datalist[4]
    l = graph.get('pos6')
    l[1] = datalist[5]
    l = graph.get('pos7')
    l[1] = datalist[6]
    l = graph.get('pos8')
    l[1] = datalist[7]
    l = graph.get('pos9')
    l[1] = datalist[8]
    l = graph.get('pos10')
    l[1] = datalist[9]
    l = graph.get('pos11')
    l[1] = datalist[10]
    l = graph.get('pos12')
    l[1] = datalist[11]
    l = graph.get('pos13')
    l[1] = datalist[12]
    l = graph.get('pos14')
    l[1] = datalist[13]
    l = graph.get('pos15')
    l[1] = datalist[14]
    l = graph.get('pos16')
    l[1] = datalist[15]
    l = graph.get('pos17')
    l[1] = datalist[16]
    l = graph.get('pos18')
    l[1] = datalist[17]
    l = graph.get('pos19')
    l[1] = datalist[18]
    l = graph.get('pos20')
    l[1] = datalist[19]
    l = graph.get('pos21')
    l[1] = datalist[20]
    l = graph.get('pos22')
    l[1] = datalist[21]
    l = graph.get('pos23')
    l[1] = datalist[22]
    l = graph.get('pos24')
    l[1] = datalist[23]
    l = graph.get('pos25')
    l[1] = datalist[24]
    l = graph.get('pos26')
    l[1] = datalist[25]
    l = graph.get('pos27')
    l[1] = datalist[26]
    l = graph.get('pos28')
    l[1] = datalist[27]
    l = graph.get('pos29')
    l[1] = datalist[28]
    l = graph.get('pos30')
    l[1] = datalist[29]
    l = graph.get('pos31')
    l[1] = datalist[30]
    l = graph.get('pos32')
    l[1] = datalist[31]
    l = graph.get('pos33')
    l[1] = datalist[32]
    l = graph.get('pos34')
    l[1] = datalist[33]
    l = graph.get('pos35')
    l[1] = datalist[34]
    l = graph.get('pos36')
    l[1] = datalist[35]
    l = graph.get('pos37')
    l[1] = datalist[36]
    l = graph.get('pos38')
    l[1] = datalist[37]
    l = graph.get('pos39')
    l[1] = datalist[38]
    l = graph.get('pos40')
    l[1] = datalist[39]
    l = graph.get('pos41')
    l[1] = datalist[40]
    l = graph.get('pos42')
    l[1] = datalist[41]
    l = graph.get('pos43')
    l[1] = datalist[42]
    l = graph.get('pos44')
    l[1] = datalist[43]
    l = graph.get('pos45')
    l[1] = datalist[44]
    l = graph.get('pos46')
    l[1] = datalist[45]
    l = graph.get('pos47')
    l[1] = datalist[46]
    l = graph.get('pos48')
    l[1] = datalist[47]
    l = graph.get('pos49')
    l[1] = datalist[48]
    l = graph.get('pos50')
    l[1] = datalist[49]
    l = graph.get('pos51')
    l[1] = datalist[50]
    l = graph.get('pos52')
    l[1] = datalist[51]
    l = graph.get('pos53')
    l[1] = datalist[52]
    l = graph.get('pos54')
    l[1] = datalist[53]

    coords = [(ch[0], ch[1]) for ch in graph.values()]
    xmin = min(c[0] for c in coords)
    xmax = max(c[0] for c in coords)
    kx = (WIDTH - 1)  / (xmax - xmin)

    ymin = min(c[1] for c in coords)
    ymax = max(c[1] for c in coords)
    if (ymax - ymin) != 0:
        ky = (HEIGHT - 1) / (ymax - ymin)

        acoords = [(round((c[0] - xmin) * kx),
                round((c[1] - ymin) * ky)) for c in coords]

        if settings.colors_on:
            print(settings.GREY)
            print("career-so-far /==================================")
            print(settings.RESET)
        else:
            print("career-so-far /==================================")
        for y in range(HEIGHT, -1, -1):
            chars = []
            for x in range(WIDTH):
                if (x, y) in acoords:
                    chars.append(MARKER)
                else:
                    chars.append(FILL_CHARACTER)
            print(''.join(chars))
        if settings.colors_on:
            print(settings.GREY)
            print("==================================/ end-of-report")
            print(settings.RESET)
        else:
            print("==================================/ end-of-report")