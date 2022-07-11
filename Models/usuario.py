'''
Autores: Vítor Augusto Ueno Otto e Leonardo de Souza Fiamoncini
'''

from Config.config import *

from Models.pessoa import Pessoa

import sys
from sys import getsizeof


class Usuario(Pessoa):
    '''
    Uma classe que representa um usuário genérico. 
    É uma pessoa com alguns atributos adicionais 
    Atributos Herdados:
    ----------
    cpf (str): cpf da pessoa (PK)
    nome (str): nome da pessoa
    dataNascimento (str): nome do bairro do endereço
    endereco_id (int): chave estrangeira, o id do endereco da pessoa
    endereco (Endereco): dado do tipo Endereco (relationship) 
    Atributos Próprios:
    ----------
    login (str): login do usuário (usado para acessar a conta)  
    senha (str): senha do usuário (usado para acessar a conta)  
    email (str): email de contato do usuário
    telefone (str): número do telefone de contato do usuário
    '''

    id = db.Column(db.Integer, db.ForeignKey('Pessoa.id', ondelete="CASCADE"), primary_key=True)
    login = db.Column(db.String(254))
    email = db.Column(db.String(254))
    telefone = db.Column(db.String(254))
    senha = db.Column(db.String(254))

    # definições de mapeamento da classe mãe
    __mapper_args__ = {
        'polymorphic_identity': 'usuario',
    }

    # calcula o tamanho dos atributos do usuario e soma com os da pessoa
    def tamanho(self):
        return (sys.getsizeof(self.id) + sys.getsizeof(self.login)
         + sys.getsizeof(self.email) + sys.getsizeof(self.telefone) 
         + sys.getsizeof(self.senha) + super().tamanho())   

    def __str__(self):
        return super().__str__() + f'\nLogin: {self.login} - ' +\
            f'Email: {self.email} - Telefone: {self.telefone}'