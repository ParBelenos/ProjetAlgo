import pygame as pg
import random as rd

pg.init()

window = pg.display.set_mode((450, 550))
font = pg.font.SysFont("arial", 36)

field = [[0, 0, 0, 0], 
         [0, 0, 0, 0], 
         [0, 0, 0, 0], 
         [0, 0, 0, 0]]

running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    window.fill("white")
    
    # CODE
    
    zero_position = [
        (r,c)
        for r, row in enumerate(field)
        for c, val in enumerate(row)
        if val == 0
    ]

    window.fill((158, 146, 135))


    # Draw background tiles
    for i in range(4):
        for j in range(4):
            pg.draw.rect(window, (205, 192, 180), (j*100+30, i*100+10, 90, 90), 0, 8)












    pg.display.flip()



pg.quit()
