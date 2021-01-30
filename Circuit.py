import pygame
from NodoCircuito import *
from Componentes import *

'''
Circuit: clase que se encarga de dibujar el circuito y sus diferentes componentes

Atributos:
length(int), width(int), exponencial(int), divisionLimit(int)
Nodos(lista), Divisiones(lista), Resistencias(lista), FuentesPoder(lista),
rect(pygame.Rect), subrect(pygame.Rect)

Metodos:
/draw_circuit(superficie, x, y):Dibuja el circuito en la posicion (x,y) de la superficie
/draw_nodos(lista,superficie): recibe una lista de nodos y los dibuja en la superficie
/draw_divisiones(superficie): dibuja objetos en self.Divisiones en la superficie 
/draw_componentes(superficie): dibuja objetos en self.Resistencias y self.FuentesPoder en superficie
/nodos_vacio(): retorna bool si self.Nodos == []
/create_nodos(): crea los primeros 4 Nodos del circuito y los inserta en self.Nodos
/crear_division(nodo):
    1.Crea una division en la posicion del nodo seleccionado y lo inserta en self.Divisiones
    2.Elimina el nodo seleccionado y su pareja
    3.Crea cuatro nuevos nodos segun posiciones calcudas con exponencial y divisionLimit
    4.Inserta los 4 nodos en self.Nodos
/search_direccion(nodo,lista,indice): recibe un nodo y una lista y retorno un string con los indices de la ubicacion del nodo separados por #
/crear_resistencia(nodo): recibe un nodo y crea una resistencia en su posicion
/crear_fuentePoder(nodo): recibe un nodo y crea una resistencia en su posicion
/getNodos(): retorna self.Nodos
/getResistencias(): retorna self.Resistencias
/getFuentesPoder(): retorna self.FuentesPoder
'''


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
            topNodo = NodoCircuito(self.rect.midtop,20)
            bottomNodo = NodoCircuito(self.rect.midbottom,20)
            leftNodo = NodoCircuito(self.rect.midleft,20)
            rightNodo = NodoCircuito(self.rect.midright,20)
            topNodo.set_divisible(True)
            bottomNodo.set_divisible(True)
            nodo = [topNodo, bottomNodo]
            self.Nodos = [rightNodo, leftNodo, nodo]
        except Exception as x:
            print(x)

    def crear_division(self,nodo):
        #Creacion de la division
        division_circuito = Division((nodo.get_rect().centerx,self.rect.y),
                            (nodo.get_rect().centerx,self.rect.y + self.width))
        #Numero de divisiones
        lenght = 0
        for division in self.Divisiones:
            lenght += 1
        #Segun numero de division se hacen cambios a exponencial y divisionLimit
        if lenght >= self.divisionLimit:
            self.exponencial *= 2
            self.divisionLimit = (self.divisionLimit * 2) +1
            print(self.exponencial,self.divisionLimit)
        #Se crean todo los nuevos nodos(5)
        nodoMedio = NodoCircuito((nodo.get_rect().centerx,self.rect.centery),20)
        direccion_nodo = self.search_direccion(nodo, self.Nodos,0)
        lista_direccion = direccion_nodo.split("#")
        nodoTop1 = NodoCircuito((nodo.get_rect().x + self.length//self.exponencial,self.rect.y),20)
        nodoTop2 = NodoCircuito((nodo.get_rect().x - self.length//self.exponencial,self.rect.y),20)
        nodoBottom1 = NodoCircuito((nodo.get_rect().x + self.length//self.exponencial,self.rect.y + self.rect.height),20)
        nodoBottom2 = NodoCircuito((nodo.get_rect().x - self.length//self.exponencial,self.rect.y + self.rect.height),20)
        #Se hacen cuatro nodos divisibles
        lista = [nodoTop1,nodoTop2,nodoBottom1,nodoBottom2]
        for nodo in lista:
            nodo.set_divisible(True)
        nodoMedio.set_divisible(False)
        #Se insertan nodos en self.Nodos
        ubicacion = self.Nodos
        copia = lista_direccion
        while copia[0] != lista_direccion[-2]:
            ubicacion = ubicacion[int(copia[0])]
            copia = copia[1:]
        ubicacion[int(lista_direccion[-2])] = [[nodoTop1,nodoBottom1],[nodoTop2,nodoBottom2]]

        #Se inserta nodo no divisible y division
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
        if nodo.get_rect().centery == self.rect.centery:
            resistencia.set_image(pygame.transform.rotate(Resistencia.img,90))
        else:
            resistencia.set_image(Resistencia.img)
        resistencia.set_rect(pygame.Rect(0,0,resistencia.get_image().get_width(),resistencia.get_image().get_height()))
        resistencia.get_rect().center = nodo.get_rect().center 
        self.Resistencias.append(resistencia)

    def crear_fuentePoder(self,nodo):
        fuentePoder = FuentePoder(0)
        fuentePoder.get_rect().center = nodo.get_rect().center
        if nodo.get_rect().centery == self.rect.y:
            fuentePoder.set_image(pygame.transform.rotate(FuentePoder.img,-90))
        elif nodo.get_rect().centery == self.rect.y + self.width:
            fuentePoder.set_image(pygame.transform.rotate(FuentePoder.img,90))
        elif nodo.get_rect().center == self.rect.midright:
            fuentePoder.set_image(pygame.transform.rotate(FuentePoder.img,180))
        else:
            fuentePoder.set_image(FuentePoder.img)
        self.FuentesPoder.append(fuentePoder)

    def getNodos(self):
        return self.Nodos

    def getResistencias(self):
        return self.Resistencias

    def getFuentesPoder(self):
        return self.FuentesPoder
                    
                    
