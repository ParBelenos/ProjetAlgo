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
game_started = False
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
            # Arrow keys
            elif event.key == pg.K_UP:
                direction = "up"
                res1 = [[],[],[],[]]
                res2 = [[],[],[],[]]
                res_temp = []
                res3 = [[],[],[],[]]
                nb_temp = [[],[],[],[]]

                for a in range(4):
                    for b in range(4):
                        res_temp.append(field[b][a])
                    res1[3-a] = res_temp
                    res_temp = []
                        
                
                for k in range(4):
                    for l in range(len(res1[k])-1):
                        if res1[k][l] == res1[k][l+1]:
                            res2[k].append(res1[k][l]*2)
                            res1[k][l+1] = 0
                        else:
                            res2[k].append(res1[k][l])
                            
                for o in range(4):
                    if len(res1[o]) == 1:
                        res2[o] = res1[o]
                    elif len(res1[o])!= 0:
                        if res1[o][-1] != res1[o][-2]:
                            nb_temp[o].append(res1[o][-1])
                
                for e in range(4):
                    res2[e] = [f for f in res2[e] if f != 0]
                
                
                
                for r in range(4):
                    if nb_temp[r] != []:
                        res2[r].append(nb_temp[r][0])
                
                for m in range(4):
                    for n in range(4-len(res2[m])):
                        res2[m].append(0)
                        
                for c in range(4):
                    for d in range(4):
                        res_temp.append(res2[3-d][c])
                    res3[c] = res_temp
                    res_temp = []
                        
                
                field = res3
                add_number()
            

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
