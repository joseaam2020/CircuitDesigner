import pygame

class Resistencia:

    img = None
    
    def __init__(self, valor):
        self.valor = valor
        self.nombre = ""
        self.rect = pygame.Rect(0,0,Resistencia.img.get_width(),Resistencia.img.get_height())
        
    @staticmethod
    def set_img(image):
        Resistencia.img = image
        print("Set resistencia")
        
    def draw_resistencia(self,superficie):
        try:
            superficie.blit(Resistencia.img,self.rect.topleft)
        except Exception as x:
            print(x)

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

class FuentePoder:

    img = None
    
    def __init__(self, valor):
        self.valor = valor
        self.nombre = ""
        self.rect = pygame.Rect(0,0,FuentePoder.img.get_width(),FuentePoder.img.get_height())

    @staticmethod
    def set_img(image):
        FuentePoder.img = image
        print("Set Poder")    

    def draw_fuentePoder(self,superficie):
        try:
            superficie.blit(FuentePoder.img,self.rect.topleft)
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
        
