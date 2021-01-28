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
        self.exponencial = 4
        self.divisionLimit = 0
        
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
            topNodo = NodoCircuito(self.rect.midtop,10)
            bottomNodo = NodoCircuito(self.rect.midbottom,10)
            leftNodo = NodoCircuito(self.rect.midleft,10)
            rightNodo = NodoCircuito(self.rect.midright,10)
            topNodo.set_divisible(True)
            topNodo.set_divisible(True)
            nodo = [topNodo, bottomNodo]
            self.Nodos = [rightNodo, leftNodo, nodo]
        except Exception as x:
            print(x)

    def crear_division(self,nodo):  
        
        lenght = 0
        for division in self.Divisiones:
            lenght += 1
            
        if lenght > self.divisionLimit:
            self.exponencial *= 2
            self.divisionLimit = (self.divisionLimit * 2) +1
            
        nodoMedio = NodoCircuito((nodo.get_rect().x,self.rect.centery),10)
        lista_nodo = self.search_contenedor(nodo, self.Nodos)
        nodoTop1 = NodoCircuito((nodo.get_rect().x + self.length//self.exponencial,self.rect.y),10)
        nodoTop2 = NodoCircuito((nodo.get_rect().x - self.length//self.exponencial,self.rect.y),10)
        nodoBottom1 = NodoCircuito((nodo.get_rect().x + self.length//self.exponencial,self.rect.y + self.rect.height),10)
        nodoBottom2 = NodoCircuito((nodo.get_rect().x - self.length//self.exponencial,self.rect.y + self.rect.height),10)
        lista_nodo = [[nodoTop1,nodoBottom1],[nodoTop2,nodoBottom2]]
        self.Nodos.append(nodoMedio)

        
    def search_contenedor(self,nodo,lista,):
        if lista == []:
            return
        else:
            if lista[0] == nodo:
                return lista
            else:
                if isinstance(lista[0],list):
                    result = self.search_contenedor(nodo,lista[0])
                    if result:
                        return result
                return self.search_contenedor(nodo, lista[1:])

    def getNodos(self):
        return self.Nodos
    
                    
                    
