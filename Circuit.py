import pygame
from NodoCircuito import *
from Componentes import *

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
        self.Resistencias = []
        self.FuentesPoder = []
        self.rect = None
        self.subrect = None
        self.nextNodox = 0
        self.exponencial = 2
        self.divisionLimit = 0
        
    def draw_circuit(self,superficie,x,y):
        self.rect = pygame.Rect(x,y,self.length,self.width)
        self.subrect = pygame.Rect(x+5,y+5,self.length-10,self.width-10)
        pygame.draw.rect(superficie, (0,0,0), self.rect)
        pygame.draw.rect(superficie, (224,224,224),self.subrect)

        if self.Nodos == []:
            self.create_nodos()

        if self.Divisiones != []:
            self.draw_divisiones(superficie)

        self.draw_nodos(self.Nodos, superficie)

        self.draw_componentes(superficie)
        

    def draw_nodos(self,lista,superficie):
        if lista == []:
            return
        else:
            if isinstance(lista[0],list):
                self.draw_nodos(lista[0],superficie)
            else:
                lista[0].draw_nodo(superficie)
            self.draw_nodos(lista[1:],superficie)

    def draw_divisiones(self,superficie):
        for division in self.Divisiones:
            division.draw_division(superficie)

    def draw_componentes(self,superficie):
        for resistencia in self.Resistencias:
            resistencia.draw_resistencia(superficie)

        for fuentePoder in self.FuentesPoder:
            fuentePoder.draw_fuentePoder(superficie)

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
            bottomNodo.set_divisible(True)
            nodo = [topNodo, bottomNodo]
            self.Nodos = [rightNodo, leftNodo, nodo]
        except Exception as x:
            print(x)

    def crear_division(self,nodo,superficie):
        division_circuito = Division((nodo.get_rect().centerx,self.rect.y),
                            (nodo.get_rect().centerx,self.rect.y + self.width))
        
        lenght = 0
        for division in self.Divisiones:
            lenght += 1
            
        if lenght >= self.divisionLimit:
            self.exponencial *= 2
            self.divisionLimit = (self.divisionLimit * 2) +1
            print(self.exponencial,self.divisionLimit)
            
        nodoMedio = NodoCircuito((nodo.get_rect().centerx,self.rect.centery),10)
        direccion_nodo = self.search_direccion(nodo, self.Nodos,0)
        lista_direccion = direccion_nodo.split("#")
        nodoTop1 = NodoCircuito((nodo.get_rect().x + self.length//self.exponencial,self.rect.y),10)
        nodoTop2 = NodoCircuito((nodo.get_rect().x - self.length//self.exponencial,self.rect.y),10)
        nodoBottom1 = NodoCircuito((nodo.get_rect().x + self.length//self.exponencial,self.rect.y + self.rect.height),10)
        nodoBottom2 = NodoCircuito((nodo.get_rect().x - self.length//self.exponencial,self.rect.y + self.rect.height),10)

        lista = [nodoTop1,nodoTop2,nodoBottom1,nodoBottom2]
        for nodo in lista:
            nodo.set_divisible(True)
        nodoMedio.set_divisible(False)  
        ubicacion = self.Nodos
        copia = lista_direccion
        while copia[0] != lista_direccion[-2]:
            ubicacion = ubicacion[int(copia[0])]
            copia = copia[1:]
        ubicacion[int(lista_direccion[-2])] = [[nodoTop1,nodoBottom1],[nodoTop2,nodoBottom2]]
        self.Nodos.append(nodoMedio)
        self.Divisiones.append(division_circuito)

        
    def search_direccion(self,nodo,lista,indice):
        if lista == []:
            return 
        else:
            if lista[0] == nodo:
                return str(indice)
            else:
                if isinstance(lista[0],list):
                    result = self.search_direccion(nodo,lista[0],0)
                    if result:
                        return str(indice) + "#" + result 
                return self.search_direccion(nodo, lista[1:],indice+1)

    def crear_resistencia(self,nodo):
        resistencia = Resistencia(0)
        resistencia.get_rect().center = nodo.get_rect().center
        self.Resistencias.append(resistencia)

    def crear_fuentePoder(self,nodo):
        fuentePoder = FuentePoder(0)
        fuentePoder.get_rect().center = nodo.get_rect().center
        print(fuentePoder.get_rect().center,fuentePoder.get_rect().topleft)
        self.FuentesPoder.append(fuentePoder)

    def getNodos(self):
        return self.Nodos
    
                    
                    
