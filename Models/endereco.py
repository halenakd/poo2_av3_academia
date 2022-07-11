from Config.config import *
import sys
from sys import getsizeof

class Endereco (db.Model):

    '''
    Uma classe que representa o endereco da pessoa.
    ...
    Atributos
    ----------
    id (int):  id numérico do endereco (PK)
    numero (str): numero da residencia
    logradouro (str): logradouro da residencia
    cep (str): cep da residencia
    bairro (str): bairro da residencia
    estado (str): estado da residencia
    pais (str): pais da residencia

    Metodos
    -------
    '''

    __tablename__ = 'Endereco'

    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(254))
    logradouro = db.Column(db.String(254))
    bairro = db.Column(db.String(254))
    cep = db.Column(db.String(254))
    estado = db.Column(db.String(254))
    pais = db.Column(db.String(254))

    # método para expressar o endereco em forma de texto
    def __str__(self):
        return f'{self.numero}, {self.logradouro}, '+\
               f'{self.bairro}, {self.cep}, '+\
               f'{self.estado}, {self.pais}'