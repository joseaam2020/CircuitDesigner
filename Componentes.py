import pygame


"""
Resistencia:

Atributos:
valor(int),
nombre(string),
rect(pygame.Rect),
*statico* img(pygame.Surface)

Metodos:
/*statico* set_img(image): recibe un pygame.Suface y lo asigna a img
/draw_resistencia(superficie): dibuja img en la superficie
/get_rect(): retorna self.rect
/set_nombre(nombre): recibe un string y lo asigna a self.nombre
/set_valor(valor): recibe un int y lo asigna a self.valor
/get_nombre(): retorna self.nombre
/get_valor(): retorna self.valor
"""


class Resistencia:

    img = None
    ohm = pygame.transform.scale(pygame.image.load("Ohms.png"),(18,18))
    
    def __init__(self, valor):
        self.valor = valor
        self.nombre = ""
        self.rect = pygame.Rect(0,0,Resistencia.img.get_width(),Resistencia.img.get_height())
        self.image = None
        
    @staticmethod
    def set_img(image):
        Resistencia.img = image
        print("Set resistencia")
        
    def draw_resistencia(self,superficie):
        try:
            font30 = pygame.font.SysFont('berlinsansfbdemi', 30)
            valores =texto(self.get_nombre() + " " + str(self.get_valor()),
                  font30,
                  (231,76,60),
                  superficie,self.rect.centerx,self.rect.midtop[1]-18,"Centro")
            superficie.blit(Resistencia.ohm,(valores.x + valores.width,valores.y))
            superficie.blit(self.image,self.rect.topleft)
        except Exception as x:
            print(x)

    def get_rect(self):
        return self.rect

    def set_rect(self,rect):
        self.rect = rect

    def set_nombre(self,nombre):
        self.nombre = nombre

    def set_valor(self,valor):
        self.valor = valor

    def get_nombre(self):
        return self.nombre

    def get_valor(self):
        return self.valor

    def set_image(self,image):
        self.image = image

    def get_image(self):
        return self.image

"""
FuentePoder:

Atributos:
valor(int),
nombre(string),
rect(pygame.Rect),
*statico* img(pygame.Surface)

Metodos:
/*statico* set_img(image): recibe un pygame.Suface y lo asigna a img
/draw_resistencia(superficie): dibuja img en la superficie
/get_rect(): retorna self.rect
/set_nombre(nombre): recibe un string y lo asigna a self.nombre
/set_valor(valor): recibe un int y lo asigna a self.valor
/get_nombre(): retorna self.nombre
/get_valor(): retorna self.valor
"""


class FuentePoder:

    img = None
    
    def __init__(self, valor):
        self.valor = valor
        self.nombre = ""
        self.rect = pygame.Rect(0,0,FuentePoder.img.get_width(),FuentePoder.img.get_height())
        self.image = None

    @staticmethod
    def set_img(image):
        FuentePoder.img = image
        print("Set Poder")    

    def draw_fuentePoder(self,superficie):
        try:
            font30 = pygame.font.SysFont('berlinsansfbdemi', 30)
            texto(self.get_nombre() + " " + str(self.get_valor()) + "V",
                      font30,
                      (231,76,60),
                      superficie,self.rect.centerx,self.rect.midtop[1]-18,"Centro")
            superficie.blit(self.image,self.rect.topleft)
        except Exception as x:
            print(x)

    def get_rect(self):
        return self.rect

    def get_rect(self):
        return self.rect

    def set_nombre(self,nombre):
        self.nombre = nombre

    def set_valor(self,valor):
        self.valor = valor

    def get_nombre(self):
        return self.nombre

    def get_valor(self):
        return self.valor

    def set_image(self,image):
        self.image = image

"""
Division:

Atributos:
posicion_incial(int,int), posicion_final(int,int)

Metodos:
/draw_division(superficie): dibuja una linea de posicion_incial a la posicion_final en superficie
"""

class Division:
    def __init__(self,posicion_inicial,posicion_final):
        self.posicion_inicial = posicion_inicial
        self.posicion_final = posicion_final
        self.color = (0,0,0)

    def draw_division(self,superficie):
        pygame.draw.line(superficie,
                         (0,0,0),
                         self.posicion_inicial,
                         self.posicion_final,
                         5)


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
        
