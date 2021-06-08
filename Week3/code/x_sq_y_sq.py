from matplotlib import cm # Para manejar colores
import numpy as np
import matplotlib.pyplot as plt

def graficar_funcion3d():
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    
    res = 100
    X = np.linspace(-4, 4, res)
    Y = np.linspace(-4, 4, res)

    X, Y = np.meshgrid(X, Y)

    #Z = X ** 2 + Y ** 2
    Z = - (X  + Y - 5)

    # Gráficar la superficie
    surf = ax.plot_surface(X, Y, Z, cmap=cm.cool, linewidth=0, antialiased=False)
    fig.colorbar(surf)
    plt.show()

def graficar_curva_nivel():
    res = 100
    X = np.linspace(-4, 4, res)
    Y = np.linspace(-4, 4, res)

    X, Y = np.meshgrid(X, Y)

    Z = np.sin(X)  

    fig2,ax2 = plt.subplots()
    level_map = np.linspace(np.min(Z), np.max(Z),res) 
    cp = ax2.contour(X, Y, Z, levels=level_map,cmap=cm.cool)
    fig2.colorbar(cp)
    ax2.set_title('Curvas de nivel')
    plt.show()

if __name__ == '__main__':
    #graficar_curva_nivel()

    graficar_funcion3d()