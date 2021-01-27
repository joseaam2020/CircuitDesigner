import pygame

#NodoCircuito: clase utilizada para visualizar las posiciones donde se pueden colocar elementos del circuito
#Atributos: rect(rectangulo de pygame), posicion (x,y), radio(int)
#Metodos:
#draw_nodo(superficie): dibuja el nodo en la superficie


#podria ser bueno poner un offset del run :v 

class NodoCircuito:
    def __init__(self, rect, posicion,radio):
        self.rect = rect
        self.posicion = posicion
        self.radio = radio

    def draw_nodo(self, superficie):
        self.rect = pygame.draw.circle(superficie, (255,255,255), self.posicion, self.radio)

    def get_rect(self):
        return self.rect
    
