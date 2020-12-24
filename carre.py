from turtle import *
def carre(taille=50, couleur='red'):
 "fonction qui dessine un carré de taille et de couleur déterminées"
 color(couleur)
 c =0
 while c <4:
    forward(taille) 
    right(90)
    c = c +1
carre(50,'red')   
def carre2():
    up()
    forward(70)
    
    down()
    carre()

carre2()



def carre3():
    up()
    forward(70)
    down()
    carre()
carre3()


