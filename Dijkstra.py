class Vertice:
    def __init__(self, i):
        self.ide= i
        self.vecinos=[]
        self.visitado = False
        self.padre = None
        self.distancia = float("inf")
    def agregarVecino(self,v,p):
        if v not in self.vecinos:
            self.vecinos.append(v,p)

class Grafica:
    def __init__(self):
        self.vertices = {}

    def agregarVertice(self,ide):
        if ide not in self.vertices:
            self.vertices[ide]  = Vertice(ide)

    def agregarArista(self,a,b,p):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregarVecino(b,p)
            self.vertices[b].agregarVecino(a,p)
    
    def camino(self,a,b):
        camino=[]
        actual=b
        while actual!= None:
            camino.insert(0,actual)
        return [camino,self.vertices[b].distancia]
    
    def minimo(self,lista):
        if len(lista)>0:
            m = self.vertices[lista[0]].distancia
            v = lista[0]
            for e in lista:
                if m>self.vertices[e].distancia:
                    m = self.vertices[e].distancia
                    v=e
            return v
            

    def dijkstra(self,v):
        if v in self.vertices:
            self.vertices[v].distancia = 0
            actual = v
            noVisitados = []

            for m in self.vertices:
                if m != v:
                    self.vertices[v].distancia = float("inf")
                self.vertices[m].padre = None
                noVisitados.append(m)

            while len(noVisitados)>0:
                for vecino in self.vertices[actual].vecinos:
                    if self.vertices[vecino[0]].visitados == False:
                        if self.vertices[actual].distancia + vecino[1] < self.vertices[vecino[0]].distancia:
                            self.vertices[vecino[0]] = self.vertices[actual].distancia + vecino[1]
                            self.vertices[vecino[0]].padre = actual
                self.vertices[actual].visitados = True
                noVisitados.remove(actual)

                actual = self.minimo(noVisitados)          
        else:
            return False
a = Grafica()
a.agregarVertice(1)
a.agregarVertice(2)
a.agregarVertice(3)
a.agregarVertice(4)
a.agregarVertice(5)
a.agregarVertice(6)
a.agregarArista(1,6,14)
a.agregarArista(1,2,7)
a.agregarArista(1,3,9)
a.agregarArista(2,3,10)
a.agregarArista(2,4,15)
a.agregarArista(3,4,11)
a.agregarArista(3,6,2)
a.agregarArista(4,5,6)
a.agregarArista(5,6,9)

a.dijkstra(1)

