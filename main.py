import pygame
from Circuit import *
from Componentes import *
from InputBox import *
from random import *
from grafo import *
from sorts import *

#Iniciando Pygame
pygame.init()

#Iniciando Ventana
window_size = (600,400)
screen = pygame.display.set_mode(size=window_size)
pygame.display.set_caption("Circuit Designer")
screen.fill((224,224,224))

#Creando fonts 
font40 = pygame.font.SysFont('berlinsansfbdemi', 40)
font35 = pygame.font.SysFont('berlinsansfbdemi', 35)
font30 = pygame.font.SysFont('berlinsansfbdemi', 30)
font15 = pygame.font.SysFont('berlinsansfbdemi', 15)

    #text(texto, font, color, superficie,x,y)
#E: un text, un tipo de font, un color(RGB),una superficie, coordenadas xy
#S: se imprime en texto con el tipo de font y color en  la superficie, coordenadas(x,y)
#R: - 
def texto(texto, font, color, superficie,x,y,posicion):
    text = font.render(texto,1,color)
    textrect = text.get_rect()
    if posicion.upper() == "CENTRO":
        textrect.midtop = (x,y)
    elif posicion.upper() == "DERECHA":
        textrect.topright = (x,y)
    else:
        textrect.topleft = (x,y)
    superficie.blit(text,textrect)
    return textrect

#Dibujando Circuito
display = pygame.Surface((500,300))
display.fill((224,224,224))
display_rect = display.get_rect()
circuit = Circuit(400,200)
circuit.draw_circuit(display, 50, 50)

#Creando Boton de simulacion
botonDisplay = pygame.Surface((500,100))
botonDisplay.fill((224,224,224))
botonSimular = pygame.draw.rect(botonDisplay,(46,204,113),(50,25,400,50))
texto("Simular", font30, (0,0,0), botonDisplay, botonSimular.midtop[0],botonSimular.midright[1]-10,"CENTRO")

#Cargando imagenes
img_resistencia = pygame.image.load("resistencia.png").convert()
img_fuentePoder = pygame.image.load("FuentePoder.png").convert()
img_resistencia.set_colorkey((255,255,255))
img_fuentePoder.set_colorkey((255,255,255))
Resistencia.set_img(img_resistencia)
FuentePoder.set_img(img_fuentePoder)

#Creando menu de seleccion
menuSeleccion = pygame.Surface((150,50))
menuSeleccion.fill((210,210,210))
menuSeleccion.blit(img_fuentePoder,(1,1))
menuSeleccion.blit(img_resistencia, (55,11))
pygame.draw.line(menuSeleccion, (0,0,0),(122,5),(122,45),6)


#Dibujando en pantalla
screen.blit(display, (50,0))
screen.blit(botonDisplay, (50,300))



#revisar_colision(lista,posicion)
#E: una lista de objetos con rectangulos y una posicion (x,y)
#S: se retorna el primer rectangulo que colisione con la posicion
#R: - 
def revisar_colision(lista,posicion):
    if lista == []:
        return 
    else:
        if isinstance(lista[0], list):
            result = revisar_colision(lista[0], posicion)
            if result:
                return result 
        else:
            if lista[0].rect.collidepoint(posicion):
                return lista[0]
        return revisar_colision(lista[1:],posicion)

#clasificar_componente(lista,top,middle,bottom,maxm,mid)
#E: una lista de objetos con rect, tres listas vacias, un maxm y mid valores de y
#S: se retorna una lista de tres listas con elementos de la lista ingresada clasificados segun maxm y mid
#R: -
def clasificar_componentes(lista,top,middle,bottom,maxm,mid):
    if lista == []:
        return [top,middle,bottom]
    else:
        if isinstance(lista[0],list):
            sublistas = clasificar_componentes(lista[0],[],[],[],maxm,mid)
            counter = 1
            for sublista in sublitas:
                counter += 1 
                for ele in sublista:
                    if counter == 1:
                        top.append(ele)
                    if counter == 2:
                        middle.append(ele)
                    if counter == 3:
                        bottom.append(ele)
        else:
            y_componente = lista[0].get_rect().centery
            print(y_componente,maxm,mid)
            if y_componente == maxm:
                top.append(lista[0])
            elif y_componente == mid:
                middle.append(lista[0])
            else:
                bottom.append(lista[0])
        return clasificar_componentes(lista[1:],top,middle,bottom,maxm,mid)

#clasificar_componente(primer_comp,componente,top,middle,bottom,conexiones,circuito)
#E: un componente, None, lista top, lista middle, lista botton, [], circuito
#S: Todas las conexiones que se puede realizar entre los componentes del circuito, empezando por componente
#R: -
def hacer_conexiones(primer_comp,componente,top,middle,bottom,conexiones,circuito):
    listas = [top,middle,bottom]
    indice = 0
    if primer_comp == componente:
        return conexiones
    else:
        if componente == None:
            componente = primer_comp

        if componente.get_rect().center == circuito.rect.midleft:
            #mas cerca arriba
            der = lambda y1,y2: y1 < y2
            newx = componente_cercano(componente.get_rect().center,top,der)
            new = buscar_componente(newx,componente.get_rect().center,top,der)
            print(new,"midleft")
            conexiones.append([componente.get_nombre(),new.get_nombre()])
            return hacer_conexiones(primer_comp,new,top,middle,bottom,conexiones,circuito)
            
        elif componente.get_rect().center[1] == circuito.rect.y:
            print(componente,"up")
            #Mas cerca derecha (arriba y abajo)
            der = lambda y1,y2: y1 < y2
            new1x = componente_cercano(componente.get_rect().center,top,der)
            new2x = componente_cercano(componente.get_rect().center,middle,der)
            if new2x and new1x:
                new1 = buscar_componente(new1x,componente.get_rect().center,top,der)
                new2 = buscar_componente(new2x,componente.get_rect().center,middle,der)
                if new2.get_rect().centerx > new1.get_rect().centerx:
                    #no hay conexion con new2
                    conexiones.append([componente.get_nombre(),new1.get_nombre()])
                else:
                    #si hay conexion
                    conexiones.append([componente.get_nombre(),new1.get_nombre()])
                    conexiones.append([componente.get_nombre(),new2.get_nombre()])
                return hacer_conexiones(primer_comp,new1,top,middle,bottom,conexiones,circuito)
            elif new2x:
                #hacer conexion
                new2 = buscar_componente(new2x,componente.get_rect().center,middle,der)
                conexiones.append([componente.get_nombre(),new2.get_nombre()])
                return hacer_conexiones(primer_comp,new2,top,middle,bottom,conexiones,circuito)
                
        elif componente.get_rect().center == circuito.rect.midright:
            print(componente,"right")
            #mas cerca a la izquierda
            izq = lambda y1,y2: y1 > y2
            newx = componente_cercano(componente.get_rect().center,bottom,izq)
            new = buscar_componente(newx,componente.get_rect().center,bottom,izq)
            print(newx,new)
            #hacer conexion
            conexiones.append([componente.get_nombre(),new.get_nombre()])
            return hacer_conexiones(primer_comp,new,top,middle,bottom,conexiones,circuito)
            
        elif componente.get_rect().center[1] == (circuito.rect.y + circuito.width):
            print(componente,"down")
            #mas cerca a la izquierda (arriba y abajo)
            izq = lambda y1,y2: y1 > y2
            new1x = componente_cercano(componente.get_rect().center,bottom,izq)
            new2x = componente_cercano(componente.get_rect().center,middle,izq)
            if new2x and new1x:
                new1 = buscar_componente(new1x,componente.get_rect().center,bottom,izq)
                new2 = buscar_componente(new2x,componente.get_rect().center,middle,izq)
                if new2.get_rect().centerx < new1.get_rect().centerx:
                    #no hay conexion
                    conexiones.append([componente.get_nombre(),new1.get_nombre()])
                else:
                    #si hay conexion
                    conexiones.append([componente.get_nombre(),new1.get_nombre()])
                    conexiones.append([componente.get_nombre(),new2.get_nombre()])
                return hacer_conexiones(primer_comp,new1,top,middle,bottom,conexiones,circuito)
            elif new2x:
                #hacer conexion
                new2 = buscar_componente(new2x,componente.get_rect().center,middle,izq)
                conexiones.append([componente.get_nombre(),new2.get_nombre()])
                return hacer_conexiones(primer_comp,new2,top,middle,bottom,conexiones,circuito)
        else:
            #mas arriba (izquierda y derecha)
            izq = lambda y1,y2: y1 > y2
            der = lambda y1,y2: y1 < y2
            new1x = componente_cercano(componente.get_rect().center,top,der)
            new2x = componente_cercano(componente.get_rect().center,top,izq)
            new1 = buscar_componente(new1x,componente.get_rect().center,top,der)
            new2 = buscar_componente(new2x,componente.get_rect().center,top,izq)
            #hacer conexion
            conexiones.append([componente.get_nombre(),new1.get_nombre()])
            conexiones.append([componente.get_nombre(),new2.get_nombre()])
            return hacer_conexiones(new2,new1,top,middle,bottom,conexiones,circuito)

#componente_cercano(posicion,listas,funcion)
#E: posicion(x,y) del componentes al que se va a comparar, lista de componentes y una funcion
#S: menor diferencia que se encontro entre componentes
#R: -
def componente_cercano(posicion,lista,funcion):
    if lista[1:] == []:
        if funcion(posicion[0],lista[0].get_rect().centerx):
            return abs(lista[0].get_rect().centerx - posicion[0])
        else:
            return None
    else:
        if funcion(posicion[0],lista[0].get_rect().x):
            return compara_menor(abs(lista[0].get_rect().centerx - posicion[0]),componente_cercano(posicion,lista[1:],funcion))
        else:
            return compara_menor(None,componente_cercano(posicion,lista[1:],funcion))
        
#compara_menor(x,y)
#E: dos int 
#S: el mayor de los int
#R: -
def compara_menor(x,y):
    if not x:
        return y
    if not y:
        return x
    if x > y:
        return y
    else:
        return x
#buscar_componente(diferencia,posicion,lista,funcion)
#E: diferencia(int) y una lista de componentes 
#S: el componente con es diferencia
#R: -
def buscar_componente(diferencia,posicion,lista,funcion):
    if lista == []:
        return
    else:
        centerx = lista[0].get_rect().centerx
        if abs(centerx-posicion[0]) == diferencia and funcion(posicion[0],centerx):
            return lista[0]
        else:
            return buscar_componente(diferencia,posicion,lista[1:],funcion)
        
#El ciclo principal
running = True
seleccionado = False
nodo = None
while running:

    #Ciclo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            x,y = mouse_pos

            
            #Si se toca boton simular:
            if botonSimular.collidepoint((x-50),y-300):
                #Consiguiendo lista de componentes segun posicion en circuito
                fuente = circuit.getFuentesPoder()[0]
                top_components,middle_components,bottom_components = clasificar_componentes(circuit.getResistencias(),[],[],[],circuit.rect.y,circuit.rect.centery)
                top_fuentes,middle_fuentes,bottom_fuentes = clasificar_componentes(circuit.getFuentesPoder(),[],[],[],circuit.rect.y,circuit.rect.centery)
                for ele in top_fuentes:
                    top_components.append(ele)
                    
                for ele in middle_fuentes:
                    middle_components.append(ele)
                    
                for ele in bottom_fuentes:
                    bottom_components.append(ele)
                print(top_components,middle_components, bottom_components)
                #Leyendo conexiones para el grafo
                conexiones = hacer_conexiones(fuente,None,top_components,middle_components,bottom_components,[],circuit)
                resistencias = circuit.getResistencias()
                fuentesPoder = circuit.getFuentesPoder()
                lista_resistencias = []
                lista_resistencias2 = []

                grafo = Grafo()

                for resistencia in resistencias:
                    grafo.agregar_vertices(resistencia.get_nombre(),"Resistencia")

                for fuentePoder in fuentesPoder:
                    grafo.agregar_vertices(fuentePoder.get_nombre(),"Fuente")

                for conexion in conexiones:
                    peso = randint(1,11)
                    grafo.agregar_arista(conexion[0],conexion[1],peso,True)

                grafo.imprimir_matriz(grafo.matriz,True)

                for resistencia in circuit.getResistencias():
                    lista_resistencias.append(resistencia.get_valor())
                    lista_resistencias2.append(resistencia.get_valor())

                insertionSort(lista_resistencias)
                print(lista_resistencias)

                quickSort(lista_resistencias2, 0, len(lista_resistencias2)-1) 
                print(lista_resistencias2)
                
                #Crear grafo A 
                #Crear listas mayor a menor, menor a mayor de nombre J A
                #Enseñar tension e intensidad J
                #Guardar grafo en archivo
            
            if not seleccionado: #Si no hay nada seleccionado, se revisan colisiones
                x,y = [x-50,y]
                nodo = revisar_colision(circuit.getNodos(), (x,y))
                resistencia = revisar_colision(circuit.getResistencias(),(x,y))
                fuentePoder = revisar_colision(circuit.getFuentesPoder(),(x,y))

                if nodo and not(fuentePoder or resistencia): #Si solo hay colision con un nodo se muestra el menu que se creo en linea 58
                    seleccionado = True
                    try:
                        menu = screen.blit(menuSeleccion,(nodo.get_rect().x,nodo.get_rect().y))
                    except Exception as x:
                        print(x)
                        
                if fuentePoder or resistencia: 
                    #Si hay colision con resistencia o fuentePoder se crea un menu para ingresar nombre y valor
                    print("Colision Fuente Poder")

                    #Creando Menu
                    menu = pygame.Surface((200,200))
                    txt1 = texto("Nombre:", font30, (0,0,0), menu, 25, 25, "")
                    txt2 = texto("Valor:", font30, (0,0,0), menu, 25, 50, "")
                    ib1 = InputBox(font30,(0,0,0),(25+txt1.width,25),7)
                    ib2 = InputBox(font30,(0,0,0),(25+txt2.width,50),7)
                    boton1 = pygame.Rect(50,80,100,50)
                    boton2 = pygame.Rect(50,140,100,50)
                    
                    #Creando Variables
                    subRunning = True
                    cambio = False
                    aceptar = 1
                    contenido1 = ""
                    contenido2 = ""
                    
                    #Subciclo principal
                    while subRunning:

                        #Actualizando menu
                        menu.fill((200,200,200))
                        txt1 = texto("Nombre:", font30, (0,0,0), menu, 25, 25, "")
                        txt2 = texto("Valor:", font30, (0,0,0), menu, 25, 50, "")
                        pygame.draw.rect(menu, (46,204,113),boton1) #Verde
                        pygame.draw.rect(menu, (231,76,60),boton2) #Rojo
                        txt3 = texto("Aceptar",font30,(0,0,0),menu,boton1.x+10,boton1.y+15,"")
                        txt4 = texto("Cancelar",font30,(0,0,0),menu,boton2.x+5,boton2.y+15,"")
                        ib1.render_box(menu)
                        ib2.render_box(menu)

                        #Subciclo de eventos
                        for event in pygame.event.get():

                            #Escribiendo texto
                            if aceptar == 1:
                                ib1.escribir(event)
                            else:
                                ib2.escribir(event)

                            #Recibiendo click para botones
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("mouse button")
                                mouse_pos = pygame.mouse.get_pos()
                                x,y = mouse_pos
                                x,y = [x-200,y-100]
                                if boton1.collidepoint(x,y):
                                    if aceptar == 1:
                                        aceptar = 2
                                    else:
                                        if ib2.contenido.isnumeric():
                                            contenido1 = ib1.contenido
                                            contenido2 = ib2.contenido
                                            subRunning = False
                                            cambio = True
                                        else:
                                            ib2.contenido = "Numero"         
                                elif boton2.collidepoint(x,y):
                                    subRunning = False

                        #Actualizando Pantalla
                        screen.blit(menu,(200,100))
                        pygame.display.update()

                    #Poniendo valores a componentes
                    if cambio:
                        if fuentePoder:
                            fuentePoder.set_nombre(contenido1)
                            fuentePoder.set_valor(int(contenido2))
                        if resistencia:
                            resistencia.set_nombre(contenido1)
                            resistencia.set_valor(int(contenido2))


                    #Quitando menu
                    display.fill((224,224,224))
                    circuit.draw_circuit(display, 50, 50)
                    screen.fill((224,224,224))
                    screen.blit(display, (50,0))
                    screen.blit(botonDisplay, (50,300))

                    for fuentePoder in circuit.getFuentesPoder():
                        print(fuentePoder.get_nombre())
                        print(fuentePoder.get_valor())
                    for resistencia in circuit.getResistencias():
                        print(resistencia.get_nombre())
                        print(resistencia.get_valor())

                    
            else:
                #Si hubo colision con nodo anteriormente (seleccionado == true)
                # entonces se busca cual opcion se selecciona del menu de nodo
                # Nota: el circuito se encarga de mostrar todos los cambios
                try:
                    if menu.collidepoint(mouse_pos):
                        x,y = mouse_pos
                        x -= menu.x
                        n = x//50
                        if n == 0:
                            print("Crear fuente de poder")
                            circuit.crear_fuentePoder(nodo) 
                        if n == 1:
                            print("Crear resistencia")
                            circuit.crear_resistencia(nodo)
                        if n == 2:
                            print("Crear Division")
                            if nodo.get_divisible():
                                circuit.crear_division(nodo)
                            else:
                                print("No se puede")
                except Exception as x:
                    print(x)

                #Quitando Menu
                seleccionado = False
                display.fill((224,224,224))
                circuit.draw_circuit(display, 50, 50)
                screen.fill((224,224,224))
                screen.blit(display, (50,0))
                screen.blit(botonDisplay, (50,300))


                
    pygame.display.update()

pygame.display.quit()
