from borracho import Borracho_Tradicional
from coordenada import Coordenada
from campo import Campo
from bokeh.plotting import figure, show

def graficar(x, y):
    grafico = figure(title='Caminos aleatorios', x_axis_label='coordenadas en x', y_axis_label='coordenadas en y')
    grafico.line(x, y, legend_label='Coordenadas')
    
    show(grafico)

def caminata(pasos, borracho, campo):
    x = []
    y = []
    for _ in range(pasos):
        coordenadas_borracho = campo.obtener_coordenada(borracho)
        x.append(coordenadas_borracho.x)
        y.append(coordenadas_borracho.y)
        campo.mover_borracho(borracho)
    
    return x, y

def main(pasos, tipo_de_borracho):
    campo = Campo()
    borracho = tipo_de_borracho(nombre='moy')
    origen = Coordenada(0,0)
    campo.anadir_borracho(borracho, origen)

    coord_x, coord_y = caminata(pasos, borracho, campo)

    graficar(coord_x, coord_y)


if __name__ == '__main__':

    pasos = 10000

    main(pasos, Borracho_Tradicional)