import math
         
class Grafo:
    def __init__(self):
        self.vertices = []
        self.matriz = [[None]*0 for i in range(0)]
        
    #Función para imprimir la matriz del grafo en la consola
    def imprimir_matriz(self, m, texto):
        cadena = ""

        #Este for haria la parte superior de la tabla
        for c in range(len(m)):
            cadena += "\t" + str(self.vertices[c])

        cadena += "\n " + ("   -" * len(m))
        
        #Este for hace la parte izquierda de la tabla
        for f in range(len(m)):
            cadena += "\n" + str(self.vertices[f]) + " |"
            for c in range(len(m)):
                if texto:
                    cadena += "\t" + str(m[f][c])
                else:
                    if f == c and (m[f][c] is None or m[f][c] == 0):
                        cadena += "\t" + "\\"
                    else:
                        if m[f][c] is None or math.isinf(m[f][c]):
                            cadena += "\t" + "X"
                        else:
                            cadena += "\t" + str(m[f][c])

        cadena += "\n"
        print(cadena)

    def contenido_en(lista, k):
        if lista.count(k) == 0:
            return False
        return True

    def esta_en_vertices(self, v):
        if self.vertices.count(v) == 0:
            return False
        return True

    def agregar_vertices(self, v, tipo):
        if self.esta_en_vertices(v):
            return False
        # Si no esta contenido.
        self.vertices.append(v)

        # Redimensiono la matriz de adyacencia.
        # Para preparalarla para agregar más Aristas.
        filas = columnas = len(self.matriz)
        matriz_aux = [[None] * (filas+1) for i in range(columnas+1)]

        # Recorro la matriz y copio su contenido dentro de la matriz más grande
        for f in range(filas):
            for c in range(columnas):
                matriz_aux[f][c] = self.matriz[f][c]

        # aqui reajustamos la matriz vieja y la convertimos en la nueva trabajada
        self.matriz = matriz_aux
        return True

    #funcion para agregar aristas
    def agregar_arista(self, inicio, fin, valor, dirijida):
        if not(self.esta_en_vertices(inicio)) or not(self.esta_en_vertices(fin)):
            return False
        #no se deberian poder repetir el tag de las aristas
        self.matriz[self.vertices.index(inicio)][self.vertices.index(fin)] = valor

    
if __name__ == "__main__":
    g = Grafo()

    g.agregar_vertices(1,"Fuente")
    g.agregar_vertices("B","Resistencia")
    g.agregar_vertices("C","Resistencia")
    g.agregar_vertices("D","Resistencia")
    g.agregar_vertices("E","Resistencia")
    g.agregar_vertices("F","Resistencia")
    

    # Dirigido.
    g.agregar_arista(1, "B", 5, True)
    g.agregar_arista(1, "D", 5, True)
    g.agregar_arista(1, "E", 2, True)
    g.agregar_arista("A", "E", 2, True)
    g.agregar_arista("B", "C", 1, True)
    g.agregar_arista("B", "E", 1, True)
    g.agregar_arista("C", "F", 5, True)
    g.agregar_arista("D", "C", 3, True)
    g.agregar_arista("D", "E", 3, True)
    g.agregar_arista("D", "F", 4, True)
    g.agregar_arista("E", "F", 8, True)


    g.imprimir_matriz(g.matriz, True)


