import pygame

#NodoCircuito: clase utilizada para visualizar las posiciones donde se pueden colocar elementos del circuito
#Atributos: rect(rectangulo de pygame), posicion (x,y), radio(int)
#Metodos:
#draw_nodo(superficie): dibuja el nodo en la superficie


#podria ser bueno poner un offset del run :v 

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
        
    
