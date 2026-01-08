import pygame as pg
import random as rd

pg.init()

window = pg.display.set_mode((450, 550))
font = pg.font.SysFont("arial", 36)

field = [[0, 0, 0, 0], 
         [0, 0, 0, 0], 
         [0, 0, 0, 0], 
         [0, 0, 0, 0]]

show_start_text = True
running = True

# Draw background tiles
def draw_background():
    for i in range(4):
        for j in range(4):
            pg.draw.rect(window, (205, 192, 180), (j*100+30, i*100+10, 90, 90), 0, 8)

# Draw start text
def draw_start_text():
    if show_start_text:
        start_text = font.render("Press spacebar to start", True, "black")
        window.blit(start_text, (80, 500))

def start_game():
    show_start_text = False
    print(field)
    game_started = True
    for i in range(2):  # Choose two random set of coords != (ß,0)
        start_num = rd.choice([2,4])
        r, c = rd.choice(zero_position)
        field[r][c] = start_num
    return show_start_text, game_started

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            # Start game
            if event.key == pg.K_SPACE and not game_started:
                start_game()

    window.fill("white")
    
    # CODE
    
    zero_position = [
        (r,c)
        for r, row in enumerate(field)
        for c, val in enumerate(row)
        if val == 0
    ]

    window.fill((158, 146, 135))


   









    pg.display.flip()



pg.quit()
