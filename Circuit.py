import pygame
from NodoCircuito import *

#Circuit: clase que se encarga de dibujar el circuito y sus diferentes componentes
#Atributos: length(int), width(int), Nodos(lista), Divisiones(lista)
#Metodos:
#draw_circuit(superficie, x, y):
#Dibuja el circuito en la posicion (x,y) de la superficie
class Circuit:
    def __init__(self, lenght, width):
        self.length = lenght
        self.width = width
        self.Nodos = []
        self.Divisiones = []
        self.rect = None
        self.subrect = None
        self.nextNodox = 0
        
    def draw_circuit(self,superficie,x,y):
        self.rect = pygame.Rect(x,y,self.length,self.width)
        self.subrect = pygame.Rect(x+5,y+5,self.length-10,self.width-10)
        pygame.draw.rect(superficie, (0,0,0), self.rect)
        pygame.draw.rect(superficie, (224,224,224),self.subrect)

        if self.Nodos == []:
            self.create_nodos()

        self.draw_nodos(self.Nodos, superficie)

    def draw_nodos(self,lista,superficie):
        if lista == []:
            return
        else:
            if isinstance(lista[0],list):
                self.draw_nodos(lista[0],superficie)
            else:
                lista[0].draw_nodo(superficie)
            self.draw_nodos(lista[1:],superficie)

    def nodos_vacio(self):
        if self.Nodos == []:
            return True
        else:
            return False

    def create_nodos(self):
        try:
            topNodo = NodoCircuito(self.rect,self.rect.midtop,10)
            bottomNodo = NodoCircuito(self.rect,self.rect.midbottom,10)
            leftNodo = NodoCircuito(self.rect,self.rect.midleft,10)
            rightNodo = NodoCircuito(self.rect,self.rect.midright,10)
            nodo = [topNodo, bottomNodo]
            self.Nodos = [rightNodo, leftNodo, nodo]
        except Exception as x:
            print(x)

    def changeNodo(self,lista,nodo):
        if lista == []:
            print("No se encontro")
            return
        else:
            if lista[0] == nodo:
                nueva_posicion = (self.lenght // (nodo.posicion[0] - self.topleft[0])) * 2
                topNodo = NodoCircuito(self.rect, (self.length // nueva_posicion ,self.top),10)
                bottomNodo = NodoCircuito(self.rect, (self.length // nueva_posicion ,self.bottom),10)
            else:
                if isinstance(lista[0],list):
                    changeNodo(lista[0],nodo)
                changeNodo(lista[1:],nodo)

    def getNodos(self):
        return self.Nodos
    
                    
                    
