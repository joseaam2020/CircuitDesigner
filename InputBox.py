import pygame

"""
InputBox: clase que se encarga de crear editores de texto

Atributos:
font(pygame.font),
color(color RGB *tupla*),posicion(lista 2 int),
maxlen(int)

Metodos:
/render_box(superficie): dibuja el contenido del edito en la posicion de la superficie
/escribir(event): recibe un event, y si se esta escribiendo en el teclado se agregan y quitan objetos a contenido
/get_contenido(): retorna contenido como string
/set_contenido(contenido): recibe un string y lo pone en el editor
"""
class InputBox():
    def __init__(self,font,color,posicion,maxlen):
        self.font = font
        self.color = color
        self.posicion = posicion
        self.contenido = ''
        self.maxlen = maxlen

    def render_box(self,superficie):
        superficie_texto = self.font.render(self.contenido,True,self.color)
        textorect = superficie_texto.get_rect()
        self.superficie = pygame.Surface((textorect.width,textorect.height))
        self.superficie.fill((0,0,0))
        self.superficie.blit(superficie_texto,(5,5))
        superficie.blit(superficie_texto,self.posicion)

    def escribir(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.contenido = self.contenido[:-1]
            else:
                if len(self.contenido) < self.maxlen:
                    self.contenido += event.unicode

    def get_contenido(self):
        return self.contenido

    def set_contenido(self,contenido):
        self.contenido = contenido
