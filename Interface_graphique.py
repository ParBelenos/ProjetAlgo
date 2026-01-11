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

# Draw start tiles
def draw_start_tiles():
    for r, row in enumerate(field):
        for c, val in enumerate(row):
            if val == 2:
                pg.draw.rect(window, (237, 229, 218), (c*100+30, r*100+10, 90, 90), 0, 8)
            elif val == 4:
                pg.draw.rect(window, (236, 224, 200), (c*100+30, r*100+10, 90, 90), 0, 8)

def add_number():
    if any(0 in row for row in field):
        probability = rd.randint(1,10)
        if probability < 10:
            number = 2
        else:
            number = 4
        r, c = rd.choice(zero_position)
        field[r][c] = number
        print(field)
    else:
        game_over_text = font.render("Game Over", True, "black")
        window.blit(game_over_text, (80, 500))

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
            
            elif event.key == pg.K_DOWN:
                res1 = [[],[],[],[]]
                res2 = [[],[],[],[]]
                res_temp = []
                res3 = [[],[],[],[]]
                nb_temp = [[],[],[],[]]

                for a in range(4):
                    for b in range(4):
                        res_temp.append(field[3-b][a])
                    res1[a] = res_temp
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
                        res_temp.append(res2[d][c])
                    res3[3-c] = res_temp
                    res_temp = []
                        
                
                field = res3
                add_number()

            elif event.key == pg.K_RIGHT:
                res1 = [[],[],[],[]]
                res2 = [[],[],[],[]]
                nb_temp = [[],[],[],[]]
                

                
                for i in range(4):
                    for j in range(4):
                        if field[i][j] != 0 :
                            res1[i].append(field[i][j])
                
                for a in range(4):
                    res1[a] = res1[a][::-1]
            
                
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
                    res2[c] = res2[c][::-1]
        
                
                field = res2
                add_number()

            elif event.key == pg.K_LEFT:
                res1 = [[],[],[],[]]
                res2 = [[],[],[],[]]
                nb_temp = [[],[],[],[]]
                for i in range(4):
                    for j in range(4):
                        if field[i][j] != 0 :
                            res1[i].append(field[i][j])
                                
                    
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
                        nb_temp[r] = []
                
                for m in range(4):
                    for n in range(4-len(res2[m])):
                        res2[m].append(0)
                field = res2
                
                add_number()

                

# CODE
    
    zero_position = [
        (r,c)
        for r, row in enumerate(field)
        for c, val in enumerate(row)
        if val == 0
    ]

    window.fill((158, 146, 135))


    # Draw background tiles
    draw_background()

    # Draw start text
    draw_start_text()

    # Draw start tiles
    draw_start_tiles()
    
    # Draw tiles
    for r, row in enumerate(field):
        for c, val in enumerate(row):
            rectangle = pg.Rect(c*100+30, r*100+10, 90, 90)

            if val == 2:
                pg.draw.rect(window, (237, 229, 218), rectangle, 0, 8)
                text_num2 = font.render(str(val), True, (119, 113, 101))
                text_pos = text_num2.get_rect(center=rectangle.center)
                window.blit(text_num2, text_pos)
            elif val == 4:
                pg.draw.rect(window, (236, 224, 200), rectangle, 0, 8)
                text_num4 = font.render(str(val), True, (119, 113, 101))
                text_pos = text_num4.get_rect(center=rectangle.center)
                window.blit(text_num4, text_pos)
            elif val == 8:
                pg.draw.rect(window, (239, 178, 124), rectangle, 0, 8)
                text_num8 = font.render(str(val), True, "white")
                text_pos = text_num8.get_rect(center=rectangle.center)
                window.blit(text_num8, text_pos)
            elif val == 16:
                pg.draw.rect(window, (242, 150, 103), rectangle, 0, 8)
                text_num16 = font.render(str(val), True, "white")
                text_pos = text_num16.get_rect(center=rectangle.center)
                window.blit(text_num16, text_pos)
            elif val == 32:
                pg.draw.rect(window, (243, 125, 99), rectangle, 0, 8)
                text_num32 = font.render(str(val), True, "white")
                text_pos = text_num32.get_rect(center=rectangle.center)
                window.blit(text_num32, text_pos)
            elif val == 64:
                pg.draw.rect(window, (243, 95, 65), rectangle, 0, 8)
                text_num64 = font.render(str(val), True, "white")
                text_pos = text_num64.get_rect(center=rectangle.center)
                window.blit(text_num64, text_pos)
            elif val == 128:
                pg.draw.rect(window, (234, 207, 118), rectangle, 0, 8)
                text_num128 = font.render(str(val), True, "white")
                text_pos = text_num128.get_rect(center=rectangle.center)
                window.blit(text_num128, text_pos)
            elif val == 256:
                pg.draw.rect(window, (237, 203, 103), rectangle, 0, 8)
                text_num256 = font.render(str(val), True, "white")
                text_pos = text_num256.get_rect(center=rectangle.center)
                window.blit(text_num256, text_pos)
            elif val == 512:
                pg.draw.rect(window, (236, 200, 90), rectangle, 0, 8)
                text_num512 = font.render(str(val), True, "white")
                text_pos = text_num512.get_rect(center=rectangle.center)
                window.blit(text_num512, text_pos)
            elif val == 1024:
                pg.draw.rect(window, (231, 194, 87), rectangle, 0, 8)
                text_num1024 = font.render(str(val), True, "white")
                text_pos = text_num1024.get_rect(center=rectangle.center)
                window.blit(text_num1024, text_pos)
            elif val == 2048:
                pg.draw.rect(window, (230, 188, 76), rectangle, 0, 8)
                text_num2048 = font.render(str(val), True, "white")
                text_pos = text_num2048.get_rect(center=rectangle.center)
                window.blit(text_num2048, text_pos)
            



    pg.display.flip()



pg.quit()
