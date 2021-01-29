import pygame

"""
 NodoCircuito: clase utilizada para visualizar las posiciones donde se pueden colocar elementos del circuito
 
Atributos:
rect(pygame.Rect),
posicion (int,int),
radio(int),
divisible(bool)

Metodos:
/draw_nodo(superficie): dibuja el nodo en la superficie
/get_rect(): retorna self.rect
/get_divisble(): retorna self.divisble
/set_divisible(divisible): recibe un bool y asigna a divisible
"""

class NodoCircuito:
    def __init__(self,posicion,radio):
        self.rect = None
        self.posicion = posicion
        self.radio = radio
        self.divisible = False

    def draw_nodo(self, superficie):
        self.rect = pygame.draw.circle(superficie, (255,255,255), self.posicion, self.radio)

    def get_rect(self):
        return self.rect

    def get_divisible(self):
        return self.divisible

    def set_divisible(self,divisible):
        self.divisible = divisible
        
    
