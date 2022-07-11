import os, sys
from sys import getsizeof

import time
import timeit

from sqlalchemy import null
currentdir = os.path.dirname(os.path.realpath(__file__)) 
parentdir = os.path.dirname(currentdir) 
sys.path.append(parentdir)

from Config.config import *
from datetime import date
from Config.criar_tabelas import *
from Models.endereco import Endereco
from Models.pessoa import Pessoa
from Models.usuario import Usuario
from Models.colaborador import Colaborador
from Models.exercicio import Exercicio
from Models.treino import Treino
from Models.exercicioTreino import ExercicioTreino
from Models.dieta import Dieta
from Models.aluno import Aluno
from Models.professor import Professor
from Models.alimento import Alimento
from Models.dietaAlimento import DietaAlimento
from Models.dietaAluno import DietaAluno
from Models.avaliacaoFisica import AvaliacaoFisica

if os.path.exists(arquivobd): 
    os.remove(arquivobd) 

db.create_all()

'''' criando 6 exercicios '''
exercicio_1 = Exercicio(
    nome = "Supino", 
    descricao = "O praticante faz uma flexão de ombro horizontal seguida por uma extensão de cotovelo e volta", 
    series=4,
    repeticoes=12)
exercicio_2 = Exercicio(
    nome = "Agachamento", 
    descricao = "O praticante abaixa os quadris a partir de uma posição em pé e depois se levanta.",
    series=4,
    repeticoes=10)
exercicio_3 = Exercicio(
    nome = "Rosca direta", 
    descricao = "O praticante abaixa os quadris a partir de uma posição em pé e depois se levanta.",
    series=3,
    repeticoes=12)  
db.session.add(exercicio_1)
db.session.add(exercicio_2)
db.session.add(exercicio_3)
db.session.commit()


''' criando 2 treinos '''
treino_1 = Treino(
    tipo = "A",
    vezes=3,
    duracao=1)
db.session.add(treino_1)
db.session.commit()


''' ligando exercicios aos treinos '''
ExercicioTreino_1 = ExercicioTreino(
    exercicio = exercicio_1, 
    treino = treino_1)
ExercicioTreino_2 = ExercicioTreino(
    exercicio = exercicio_2, 
    treino = treino_1)
ExercicioTreino_3 = ExercicioTreino(
    exercicio = exercicio_3, 
    treino = treino_1)
db.session.add(ExercicioTreino_1)
db.session.add(ExercicioTreino_2)
db.session.add(ExercicioTreino_3)
db.session.commit()


''' criando 3 enderecos'''
endereco_1 = Endereco(
    numero = "611",
    logradouro = "Eng Odebrecht",
    bairro = "Garcia",
    cep = "89021200",
    estado = "SC",
    pais = "Brasil")
db.session.add(endereco_1)
db.session.commit()


''' criando alimentos '''
alimento_1 = Alimento(
    nome = "maca",
    tipo = "fruta")
alimento_2 = Alimento(
    nome = "alface",
    tipo = "vegetal")
alimento_3 = Alimento(
    nome = "macarrao integral",
    tipo = "vegetal")
db.session.add(alimento_1)
db.session.add(alimento_2)
db.session.add(alimento_3)
db.session.commit()


''' criando tipos de dietas '''
dieta_1 = Dieta(
    duracao = "3 meses",
    objetivo = "Emagrecimento",
    tipo = "Dukan")
db.session.add(dieta_1)
db.session.commit()


''' ligando alimentos e dietas '''
DietaAlimento_1 = DietaAlimento(
    alimento = alimento_1,
    dieta = dieta_1,
    qntd = "1 vez ao dia",
    porcao = "50g")
DietaAlimento_2 = DietaAlimento(
    alimento = alimento_2,
    dieta = dieta_1,
    qntd = "1 vez ao dia",
    porcao = "250g")
DietaAlimento_3 = DietaAlimento(
    alimento = alimento_3,
    dieta = dieta_1,
    qntd = "1 vez ao dia",
    porcao = "200g")
db.session.add(DietaAlimento_1)
db.session.add(DietaAlimento_2)
db.session.add(DietaAlimento_3)
db.session.commit()


''' criando 1 professor '''
professor_1 = Professor(
    cpf = "12345678911",
    nome = "Amadeu da Luz",
    dataNascimento = date(1980, 7, 4),
    endereco = endereco_1,
    login = "amadeu_luz",
    email = "amadeu@gmail.com",
    telefone = "98302034",
    senha = "123",
    salario = 5000,
    turno = "matutino")
db.session.add(professor_1)
db.session.commit()



# TAMANHO DOS ALUNOS
inicio = timeit.default_timer()

n = 6

''' criando alunos '''
lista_tamanhos_alunos = []
for i in range(4**n):
    aluno_1 = Aluno(
        cpf = "12345678912",
        nome = "Antonio Carlos",
        dataNascimento = date(1949, 12, 15),
        endereco = endereco_1, 
        login = "antonio_c",
        email = "antonio@gmail.com",
        telefone = "44509804",
        senha = "123",
        treino= treino_1,
        objetivo="Emagrecimento",
        professor = professor_1)
    db.session.add(aluno_1)
    db.session.commit()
    lista_tamanhos_alunos.append(aluno_1.tamanho())

print("\n------------------------ Soma de todos os atributos ------------------------")
somaTotal = sum(lista_tamanhos_alunos)
print("Valor de n:", n)
print("Somas de todas as listas:", somaTotal)

fim = timeit.default_timer()
print("Duracao: %f s" % (fim - inicio))



''' criando avaliacoes '''
avaliacao_1 = AvaliacaoFisica(
    aluno = aluno_1,
    data = date(2022, 6, 6),
    peso = 75,
    altura = 170,
    med_abdn = 85)
db.session.add(avaliacao_1)
db.session.commit()


''' ligando dietas e alunos '''
DietaAluno_1 = DietaAluno(
    aluno = aluno_1,
    dieta = dieta_1,
    data_inicio = date(2022, 1, 16))
db.session.add(DietaAluno_1)
db.session.commit()


# PRINTS
"""# mostrando professores criados
print("\nPROFESSORES")
print("------------------------")
print(professor_1)

# mostrando alunos e exercicios dos treinos dos alunos
print("\nALUNOS, TREINOS E EXERCICIOS")
for a in db.session.query(Aluno).all():
    exercicios = db.session.query(ExercicioTreino).filter_by(treino_id = a.treino.id)
    ''' print do aluno '''
    print("------------------------")
    print(a)
    ''' print do treino do aluno '''
    print(a.treino)
    ''' print dos exercicios do treino do aluno '''
    print("Exercicios:")
    for e in exercicios:
        print("- " + e.exercicio.nome)

# print dos alunos do professor
print("\nLISTAS DE ALUNOS DOS PROFESSORES")
# lista reversa
print("------------------------")
print("Alunos do professor " + professor_1.nome + ":")
for p in professor_1.alunos:
    print("- " + p.nome)

# mostrando avaliacoes fisicas dos alunos
print("\nAVALIACOES FISICAS")
print("------------------------")
print(avaliacao_1)

# mostrando dietas dos alunos
print("\nDIETAS")
for aluno in db.session.query(Aluno).all():
    dietas = db.session.query(DietaAluno).filter_by(aluno_id = aluno.id)
    # print do aluno
    print("------------------------")
    print("Aluno:", aluno.nome)
    print("Dietas:")
    for dieta in dietas:
        # print das dietas
        print(dieta.dieta.tipo)
        alimentos = db.session.query(DietaAlimento).filter_by(dieta_id = dieta.id)
        # print dos alimentos
        for alimento in alimentos:
            print("- " + alimento.alimento.nome)  """