from borracho import Borracho_Tradicional
from coordenada import Coordenada
from campo import Campo
from bokeh.plotting import figure, show
from bokeh.layouts import row

def graficar(x, y, x_label, y_label):
    grafico = figure(title='Caminos aleatorios', x_axis_label=x_label, y_axis_label=y_label)
    grafico.line(x, y, legend_label='Coordenadas')
    
    return grafico

def caminata(pasos, borracho, campo):
    x = []
    y = []
    z = []
    for _ in range(pasos):
        coordenadas_borracho = campo.obtener_coordenada(borracho)
        x.append(coordenadas_borracho.x)
        y.append(coordenadas_borracho.y)
        z.append(coordenadas_borracho.z)
        campo.mover_borracho(borracho)
    
    return x, y, z

def main(pasos, tipo_de_borracho):
    campo = Campo()
    borracho = tipo_de_borracho(nombre='moy')
    origen = Coordenada(0,0,0)
    campo.anadir_borracho(borracho, origen)

    coord_x, coord_y, coord_z = caminata(pasos, borracho, campo)

    x_label = 'Coordenadas en x'
    y_label = 'Coordenadas en y' 
    z_label = 'Coordenadas en z'
    
    grafico_1 = graficar(coord_x, coord_y, x_label, y_label)
    grafico_2 = graficar(coord_z, coord_y, z_label, y_label)
    grafico_3 = graficar(coord_x, coord_z, x_label, z_label)
    show(row(grafico_1, grafico_2, grafico_3))

if __name__ == '__main__':

    pasos = 10000

    main(pasos, Borracho_Tradicional)