
class Coordenada:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def mover(self, delta_x, delta_y, delta_z):

        return Coordenada(delta_x + self.x, delta_y + self.y, delta_z + self.z)

    def distancia(self, otra_coordenada):
        delta_x = self.x - otra_coordenada.x
        delta_y = self.y - otra_coordenada.y
        delta_z = self.z - otra_coordenada.z

        cateto_a = (delta_x**2 + delta_y**2)**0.5

        return (cateto_a**2 + delta_z**2)**0.5
