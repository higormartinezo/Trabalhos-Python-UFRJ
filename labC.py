# Higor Martinez Oliveira

#Exercicio 1

def positivo(numero):
    """Retorna o valor absoluto de um número"""
    try:
        return abs(float(numero))
    except ValueError:
        print("'%s' não pode ser convertido em um número" % numero)
        return None


#Exercicio 2

def encontraIndices(lista, elemento):
    """Retorna uma lista de índices de um elemento dentro da lista dada"""
    
    listaIndices = []
    
    try:
        list.append(listaIndices, list.index(lista, elemento))
        while len(listaIndices) < list.count(lista, elemento):
            list.append(listaIndices, list.index(lista, elemento, listaIndices[-1]+1))
        return listaIndices
    except ValueError:
        return []


#Exercicio 3

def inversos(ListaTupla):
    """Retorna o inverso dos elementos de uma lista ou tupla dada"""
    
    listaInversos = []

    for i in ListaTupla:
        try:
            list.append(listaInversos, 1/float(i))
        except ValueError:
            print("Inverso de '%s' não definido" % i)
            list.append(listaInversos, "Nan")
        except TypeError:
            print("Entrada de tipo %s não válida" % type(i))
            list.append(listaInversos, "Nan")
        except ZeroDivisionError:
            print("Divisão por zero")
            list.append(listaInversos, "Nan")
            
    return listaInversos
