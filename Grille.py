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
        res = [[],[],[],[]]
        for i in self.grille:
            for j in range(4):
                if 
                
    
    
    
Grille1 = Grille()
        
    






