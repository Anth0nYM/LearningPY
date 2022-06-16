# Abstraindo um Cilindro como uma classe
from cairo import Surface


class Cylinder(object):
    pi = 3.14159265358979323846
    def __init__(self, height=1, radius=2):
        self.height = height
        self.radius = radius

    def volume(self):
        volume = self.pi * self.radius**2 * self.height
        return(volume)

    def surface_area(self):
        area = self.pi * self.radius**2 
        return(area)
cilindro = Cylinder(9,5)
print('o volume do cilindro é {:.2f}'.format(cilindro.volume()))
print('A área do cilindro é {:.2f}'.format(cilindro.surface_area()))
