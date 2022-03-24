# Higor Martinez Oliveira

import math
import numpy as np

#Exercício 1

def calcularAngulo(x,y):
    """Funcao que retorna o angulo em graus dado o valor de seno e cosseno"""

    if x**2 + y**2 == 1:
        angulo = math.acos(y)
        if x < 0:
            anguloGraus = math.degrees(angulo-(2*angulo))
            return anguloGraus
        else:
            anguloGraus = math.degrees(angulo)
            return anguloGraus
    else:
        return None


#Exercício 2

def analisarIsometria(matriz):
    """Funcao que analisa se uma transformacao é uma isometria"""

    vetorTranslacao = matriz[:,2]
    submatrizA = np.array([[matriz[0,0], matriz[0,1]], [matriz[1,0], matriz[1,1]]])
    matrizIdentidade = np.identity(2)
    R = np.array([[1,0], [0,-1]])
        
    if np.allclose(np.transpose(submatrizA)@submatrizA, matrizIdentidade) == False:
        return "A transformacao não é uma isometria" 
    else:
        if np.linalg.det(submatrizA) < 0: #há reflexao
            matrizRot = submatrizA@np.transpose(R)
            anguloRot = calcularAngulo(matrizRot[1,0], matrizRot[0,0])
            if anguloRot != 0 and np.allclose(np.zeros(2), vetorTranslacao) == False: #rotacao != 0 com translacao
                return "A transformacao é uma isometria composta de reflexão pelo eixo x, rotação pelo ângulo {} graus, translação pelo vetor {}".format(anguloRot, vetorTranslacao)
            elif anguloRot != 0 and np.allclose(np.zeros(2), vetorTranslacao) == True: #rotacao != 0 sem translacao
                return "A transformacao é uma isometria composta de reflexão pelo eixo x, rotação pelo ângulo {} graus".format(anguloRot)
            elif anguloRot == 0 and np.allclose(np.zeros(2), vetorTranslacao) == False: #rotacao == 0 com translacao
                return "A transformacao é uma isometria composta de reflexão pelo eixo x, translação pelo vetor {}".format(vetorTranslacao)
            elif anguloRot == 0 and np.allclose(np.zeros(2), vetorTranslacao) == True: #rotacao == 0 sem translacao
                return "A transformacao é uma isometria composta de reflexão pelo eixo x"

        if np.linalg.det(submatrizA) > 0: #sem reflexao
            anguloRot = calcularAngulo(submatrizA[1,0], submatrizA[0,0])
            if anguloRot != 0 and np.allclose(np.zeros(2), vetorTranslacao) == False: #rotacao !=0 com translacao
                return "A transformacao é uma isometria composta de rotação pelo ângulo {} graus, translação pelo vetor {}".format(anguloRot, vetorTranslacao)
            elif anguloRot != 0 and np.allclose(np.zeros(2), vetorTranslacao) == True: #rotacao != 0 sem translacao
                return "A transformacao é uma isometria composta de rotação pelo ângulo {} graus".format(anguloRot)
            elif anguloRot == 0 and np.allclose(np.zeros(2), vetorTranslacao) == False: #rotacao == 0 com translacao
                return "A transformacao é uma isometria composta de translação pelo vetor {}".format(vetorTranslacao)

#Exercício 3

def comporIsometria(angulo, b = np.array([0,0]) , reflexao = False):
    """Funcao que compoe uma isometria dado o angulo, vetor de translação e condicao de reflexão"""

    A = np.array([[math.cos(angulo), -math.sin(angulo)], [math.sin(angulo), math.cos(angulo)]])

    Rx = np.array([[1,0],[0,-1]])

    if reflexao == False:
        matrizAb = np.column_stack((A, b))
    elif reflexao == True:
        A = A@Rx
        matrizAb = np.column_stack((A, b))

    return matrizAb
