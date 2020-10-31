import random

class Borracho:

    def __init__(self, nombre):
        self.nombre = nombre


class Borracho_Tradicional(Borracho):

    def __init__(self, nombre):
        super().__init__(nombre)

    def camina(self):
        return random.choice([(0,1,0), (0,-1,0), (1,0,0), (-1,0,0), (0,0,1), (0,0,-1)])
        

if __name__ == '__main__':
    borracho = Borracho_Tradicional('moy')
    print(borracho.camina())
    

        