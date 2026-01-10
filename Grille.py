from random import randint
from random import choice
class Grille():
    def __init__(self):
        self.grille = [[0,0,0,0],
                       [0,0,0,0],
                       [0,0,0,0],
                       [0,0,0,0]]

    def affiche_grille(self):
        for i in self.grille:
            print(f"{i}")

    def ajoute_nombre(self):
        a = choice([2,4])
        while a != 0:
            ligne_al = randint(0,3)
            case_al = randint(0,3)
            if self.grille[ligne_al][case_al] == 0:
                self.grille[ligne_al][case_al] = a
                a= 0

    
    def gauche(self):
        res1 = [[],[],[],[]]
        res2 = [[],[],[],[]]
        nb_temp = [[],[],[],[]]
        for i in range(4):
             for j in range(4):
                if self.grille[i][j] != 0 :
                    res1[i].append(self.grille[i][j])
                        
            
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
        self.grille = res2
        self.affiche_grille()
        
    def droite(self):
        res1 = [[],[],[],[]]
        res2 = [[],[],[],[]]
        nb_temp = [[],[],[],[]]
        

        
        for i in range(4):
         for j in range(4):
            if self.grille[i][j] != 0 :
                res1[i].append(self.grille[i][j])
        
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
        
        self.grille = res2
        self.affiche_grille()
        


    def haut(self):
        res1 = [[],[],[],[]]
        res2 = [[],[],[],[]]
        res_temp = []
        res3 = [[],[],[],[]]
        nb_temp = [[],[],[],[]]

        for a in range(4):
            for b in range(4):
                res_temp.append(self.grille[b][a])
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
                
        
        self.grille = res3
        self.affiche_grille()
        
        
    def bas(self):
        res1 = [[],[],[],[]]
        res2 = [[],[],[],[]]
        res_temp = []
        res3 = [[],[],[],[]]
        nb_temp = [[],[],[],[]]

        for a in range(4):
            for b in range(4):
                res_temp.append(self.grille[3-b][a])
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
                
        
        self.grille = res3
        self.affiche_grille()
        
        
    






