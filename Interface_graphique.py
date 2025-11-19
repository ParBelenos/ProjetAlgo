import pygame as p
from random import randint
from random import choice

p.init()

size_x, size_y = 800, 470

window = p.display.set_mode([size_y, size_y])

running = True

while running:
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False

    window.fill("white")
    
    # CODE
    
    a1 = p.draw.rect(window, "gray", (30, 30, 80, 80))
    a2 = p.draw.rect(window, "gray", (140, 30, 80, 80))
    a3 = p.draw.rect(window, "gray", (250, 30, 80, 80))
    a4 = p.draw.rect(window, "gray", (360, 30, 80, 80))

    b1 = p.draw.rect(window, "gray", (30, 140, 80, 80))
    b2 = p.draw.rect(window, "gray", (140, 140, 80, 80))
    b3 = p.draw.rect(window, "gray", (250, 140, 80, 80))
    b4 = p.draw.rect(window, "gray", (360, 140, 80, 80))
    
    c1 = p.draw.rect(window, "gray", (30, 250, 80, 80))
    c2 = p.draw.rect(window, "gray", (140, 250, 80, 80))
    c3 = p.draw.rect(window, "gray", (250, 250, 80, 80))
    c4 = p.draw.rect(window, "gray", (360, 250, 80, 80))
    
    d1 = p.draw.rect(window, "gray", (30, 360, 80, 80))
    d2 = p.draw.rect(window, "gray", (140, 360, 80, 80))
    d3 = p.draw.rect(window, "gray", (250, 360, 80, 80))
    d4 = p.draw.rect(window, "gray", (360, 360, 80, 80))
    












    p.display.flip()



p.quit()
