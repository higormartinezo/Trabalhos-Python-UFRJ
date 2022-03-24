# Higor Martinez Oliveira


# Exercicio 1

def calculeN(A1, An, r):
    """Funcao que calcula o numero de termos de uma P.A dado o valor inicial, final e a razao"""
    return ((An - A1)/r)+1

def somaPA(A1, An, r):
    """Funcao que calcula a soma de uma P.A dado o valor inicial, final e a razao"""
    return((A1 + An) * calculeN(A1, An, r))/2


# Exercicio 2

def concatena(str1, str2):
    """Funcao que concatena a primeira string sem os 5 primeiros caracteres, com a segunda sem os últimos 10 caracteres"""
    return str1[5:] + str2[:-10]


# Exercicio 3

def sublista(Lista, n):
    """Funcao que dada uma lista de números inteiros e um número inteiro, retorna uma sublista com os elementos maiores que n"""
    sublista = [ ]
    for elemento in Lista:
        if elemento > n:
            list.append(sublista, elemento)
            
    return sublista


# Exercicio 4

def primo(x):
    """Funcao que verifica se um numero natural e primo ou nao"""

    numero_divisores = 0 #Contagem inicial de divisores entre 1 e n

    for divisor in range(1,x+1):
        if x % divisor == 0:
            numero_divisores += 1
            
    if numero_divisores == 2:
        return "O numero e primo!"
    else:
        return "O numero nao e primo"


# Exercicio 5

def numeroEuler(n):
    """Funcao para calcular o número de Euler dado o n-esimo termo"""

    import math
    
    somatorio = 1 
    for i in range(1,n+1):
        somatorio = somatorio + (1/math.factorial(i)) # 1 + (1/1 +1/2....1/n)
    return somatorio

def precisaoEuler(erro):
    """Funcao que calcula o numero de termos necessarios na serie para que o erro absoluto seja inferior ao erro passado"""

    import math

    n = 0 # Valor inicial de n 

    while math.fabs(math.e - numeroEuler(n)) > math.fabs(erro):
        n = n+1

    return n

def main():

    """Funcao principal"""

    erro = float(input("Qual a precisao desejada? "))
    
    print(str.format("O numero de termos da serie que deve ser calculado e {:d}", precisaoEuler(erro)))

    if __name__ == "__main__":
        main()
          
