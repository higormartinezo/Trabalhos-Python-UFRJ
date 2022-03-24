# Higor Martinez Oliveira

import numpy as np
import matplotlib.pyplot as plt

#Exercício 1 

def logaritmos(n):
    """Gera o gráfico de ln(x) e log10(x) dado uma quantidade de números n"""

    fig, a = plt.subplots(figsize = (6,6))
    
    x = np.linspace(0.01, 2, n)
    y1 = np.log(x)
    y2 = np.log10(x)
    
    a.set_title("Logaritmos")
    a.set_xticks([0,1,2])

    a.plot(x, y1, "c-s", linewidth=2, label=r"$y=\ln(x)$")
    a.plot(x, y2, "m-o", linewidth=2, label=r"$y=\log_{10}(x)$")
    a.legend(loc="lower right")
    
    plt.savefig("logaritmos.png")
 
    return None


#Exercício 2

def polinomios(z):
    """Gera o gráfico de polinomios de 1 até um grau máximo z dado"""

    fig, a = plt.subplots(figsize = (6,6))

    x = np.linspace(-1, 1, 100)

    for i in range(1, z+1):
        y = x**i
        a.plot(x, y, "-", linewidth=2, label="x**{}".format(i))

    a.set_xticks([-1,0,1])
    a.set_yticks([-1,0,1])
    a.legend(loc="lower right")
    
    plt.savefig("polinomios.png")

    return None 


#Exercício 3

def tangente():
    """Gera o gráfico da tangente no intervalo -3pi/2 a 3pi/2"""

    fig, a = plt.subplots(figsize = (6,6))

    x = np.linspace(-3/2*np.pi, 3/2*np.pi, 100)
    y = np.tan(x)

    condA = np.hstack((np.abs(np.diff(y)) > 2, np.array([True])))
    condB = np.hstack((np.array([True]), np.abs(np.diff(y)) > 2))

    pos = np.where(condA&condB)
    y[pos] = np.nan 
     
    a.plot(x, y, "b-")
    plt.savefig("tangente.png")

    return pos
