# Higor Martinez Oliveira

class Aluno:
    def __init__(self, nome, DRE, matricula = "ativa"):
        """Cria um objeto da classe Aluno com atributos nome, DRE, matricula"""
        self.nome = nome
        self.DRE = DRE       
        self.matricula = matricula

    def trancarMatricula(self):
        """Tranca a matricula"""
        self.matricula = "trancada"
        
    def cancelarMatricula(self):
        """Cancela a matricula"""
        self.matricula = "cancelada"
        
    def reativarMatricula(self):
        """Reativa a matricula se a matricula não for cancelada"""
        if self.matricula == "cancelada":
            print("Matrícula cancelada, solicite reabertura de matrícula")
        else:
            self.matricula = "ativa"
            
    def __str__(self): # método novo
        """Retorna uma descrição de um objeto da classe"""
        return "{}, DRE {}, matricula {}\n".format(self.nome, str(self.DRE), self.matricula)


class Disciplina:
    """Classe representa o conceito de uma disciplina na UFRJ"""
    def __init__(self, nome, carga, vagas = 40):
        self.nome = nome
        self.carga = carga
        self.vagas = vagas
    
    def __str__(self):
        """Retorna uma descrição de um objeto da classe"""
        return self.nome
    
#  Herança ================================

class Monitor(Aluno):
    """Representa o conceito de um monitor"""
    def __init__(self, nome, DRE, historico = []):
        """O parametro historico deve ser uma lista de listas, onde o primeiro
        elemento da sublista é uma disciplina e o segundo elemento é o período."""
        super().__init__(nome, DRE)
        self.historico = historico

    def __str__(self):
        """Retorna uma descrição de um objeto da classe"""
        string =  Aluno.__str__(self) + "HISTÓRICO DE MONITORIA\n"
        string += "Nome da Disciplina\tCarga horária\tPeríodo de monitoria\n"
        for entrada in self.historico:
            turma = entrada[0]
            periodo = entrada[1]
            string += "{}\t\t{}\t\t{}\n".format(turma.nome, turma.carga, periodo)
        return string

    
# Exercicio 1

class Turma(Disciplina):
    """"Classe que representa o conceito de uma turma"""
    def __init__(self, nome, carga, vagas, horario, alunos = []):
        super().__init__(nome, carga, vagas)
        self.horario = horario
        self.alunos = alunos

    def __add__(self, outro):
        """Junta duas turmas de nome, carga e horario iguais"""
        if self.nome == outro.nome and self.carga == outro.carga and self.horario == outro.horario:
            return Turma(self.nome, self.carga, self.vagas + outro.vagas, self.horario, self.alunos + outro.alunos)
        elif self.nome != outro.nome and self.carga == outro.carga and self.horario == outro.horario:
            print ("Nao foi possivel juntar as turmas. Nomes tem que ser iguais.")
        elif self.nome == outro.nome and self.carga != outro.carga and self.horario == outro.horario:
            print ("Nao foi possivel juntar as turmas. Cargas tem que ser iguais.")
        elif self.nome == outro.nome and self.carga == outro.carga and self.horario != outro.horario:
            print ("Nao foi possivel juntar as turmas. Horarios tem que ser iguais.")
        elif self.nome != outro.nome and self.carga != outro.carga and self.horario == outro.horario:
            print ("Nao foi possivel juntar as turmas. Nomes tem que ser iguais. Cargas tem que ser iguais.")
        elif self.nome != outro.nome and self.carga == outro.carga and self.horario != outro.horario:
            print ("Nao foi possivel juntar as turmas. Nomes tem que ser iguais. Horarios tem que ser iguais.")
        elif self.nome == outro.nome and self.carga != outro.carga and self.horario != outro.horario:
            print ("Nao foi possivel juntar as turmas. Cargas tem que ser iguais. Horarios tem que ser iguais.")
        else:
            print ("Nao foi possivel juntar as turmas. Nomes tem que ser iguais. Cargas tem que ser iguais. Horarios tem que ser iguais.")
            
    def __str__(self):
        """Retorna os dados de um objeto da classe Turma"""
        return "{}, carga: {}, horário: {}\nvagas totais: {}, vagas livres: {}".format(self.nome, self.carga, self.horario, self.vagas, self.vagas - len(self.alunos))


# Exercicio 2

class Bolsista(Aluno):
    """Classe que representa o conceito de um bolsista"""
    def __init__(self, nome, DRE, bolsa):
        super().__init__(nome, DRE)
        self.bolsa = bolsa

    def trancarMatricula(self):
        """Tranca a matrícula e altera o valor da bolsa para 0"""
        self.matricula = "trancada"
        self.bolsa = 0
