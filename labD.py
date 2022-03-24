# Higor Martinez Oliveira

#Enunciado do trabalho em: https://drive.google.com/file/d/1K6_qpEiaW-Yv0WJLHiuTaPA3-pMVmcVp/view?usp=sharing 

#Exercicio 1

def frequenciaDomicilio(dicionario):
    """"Retorna um dicionario com a frequencia de tipos de domicilios do censo. A chave do dicionário de entrada é o CPF do respondente e os valores o tipo de domicílio"""

    dicDomicilios = {}
    for c in dicionario.values():
        if c not in dicDomicilios:
            dicDomicilios[c] = 1
        else:
            dicDomicilios[c] += 1
    return dicDomicilios


#Exercicio 2

def processaDados(dicionario):
    """Retorna o total de respondentes e o conjunto de CPFs que possui certo equipamento: tv, máquina e geladeira"""

    tv = {}
    maquina = {}
    geladeira = {}
    
    for n in dicionario.keys():
        if "tv" in dicionario.get(n):
            tv[n] = dicionario.keys()

    for n in dicionario.keys():
        if "maquina" in dicionario.get(n):
            maquina[n] = dicionario.keys()

    for n in dicionario.keys():
        if "geladeira" in dicionario.get(n):
            geladeira[n] = dicionario.keys()

    dicDados = {}
    dicDados["total"] = len(dicionario)
    dicDados["tv"] = set(tv)
    dicDados["maquina"] = set(maquina)
    dicDados["geladeira"] = set(geladeira)

    return dicDados


def eletrodomesticos(dicionario):
    """"Retorna a % de domicilios: com maquina e geladeira; sem tv; sem nenhum equipamento"""
    
    respondentes = dicionario.get("total")
    tv = dicionario.get("tv")
    maquina = dicionario.get("maquina")
    geladeira = dicionario.get("geladeira")

    caso1 = (len(maquina.intersection(geladeira))/respondentes)*100
    caso2 = ((respondentes - len(tv))/respondentes)*100
    caso3 = ((respondentes - len(tv | maquina | geladeira))/respondentes)*100

    return (caso1, caso2, caso3)
