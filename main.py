import pygame
from Circuit import *

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

#Creando menu de seleccion
menuSeleccion = pygame.Surface((150,50))
menuSeleccion.fill((210,210,210))
menuSeleccion.blit(img_fuentePoder,(1,1))
menuSeleccion.blit(img_resistencia, (55,11))
pygame.draw.line(menuSeleccion, (0,0,0),(122,5),(122,45),6)


#Dibujando en pantalla
screen.blit(display, (50,0))
screen.blit(botonDisplay, (50,300))

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
            if not seleccionado:
                x,y = [x-50,y]
                nodo = revisar_colision(circuit.getNodos(), (x,y))
                seleccionado = True
                try:
                    menu = screen.blit(menuSeleccion,(nodo.get_rect().x,nodo.get_rect().y))
                except Exception as x:
                    print(x)
                    
            else:
                try:
                    if menu.collidepoint(mouse_pos):
                        x,y = mouse_pos
                        x -= menu.x
                        n = x//50
                        print(n)
                        if n == 0:
                            print("Crear fuente de poder")
                        if n == 1:
                            print("Crear resistencia")
                        if n == 2:
                            print("Crear Division")
                            circuit.crear_division(nodo)
                except Exception as x:
                    print(x)
                    
                seleccionado = False
                display.fill((224,224,224))
                circuit.draw_circuit(display, 50, 50)
                screen.fill((224,224,224))
                screen.blit(display, (50,0))
                screen.blit(botonDisplay, (50,300))

                
    pygame.display.update()

pygame.display.quit()
