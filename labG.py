#Higor Martinez Oliveira

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

#Exercício 1

def alturas(n):
    """A entrada é n números aleatórios para gerar as alturas"""

    fig, ax = plt.subplots()
    a = st.norm.rvs(loc = 1.7, scale = 0.08, size = n)
    ax.hist(a, bins = 20, facecolor = "c")
    ax.set_title("Alturas")
    plt.savefig("alturas.png")

    return a 

    
#Exercício 2

def pesos(altura):
    """O parâmetro de entrada é um np.ndarray com as alturas de um conjunto de pessoas. Retorna o peso pelo calculo do IMC"""

    fig, ax = plt.subplots()
    imc = st.norm.rvs(loc = 24.5, scale = 4.3, size = np.size(altura))
    pesos = imc*(altura**2)
    ax.hist(pesos, bins = 20, facecolor = "m")
    ax.set_title("Pesos")
    plt.savefig("pesos.png")

    return pesos


#Exercício 3

def regressaoLinear(altura, peso):
    """Gráfico de regressao linear para a altura e peso gerados"""

    fig, ax = plt.subplots()
    
    regressao = st.linregress(altura, peso)
    x = np.linspace(altura.min(),altura.max())
    y = regressao[0]*x + regressao[1]

    ax.plot(x, y, "r")
    ax.scatter(altura, peso)

    ax.set_title("Altura vs peso")
    plt.xlabel("Altura")
    plt.ylabel("Peso")
    plt.savefig("regressao.png")

    return (regressao[0], regressao[1])
    
