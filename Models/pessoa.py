from Config.config import * 
from Models.endereco import Endereco
import sys
from sys import getsizeof

class Pessoa(db.Model):
    __tablename__ = 'Pessoa'

    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(11))
    nome = db.Column(db.String(100), nullable=False)
    dataNascimento = db.Column(db.Date(), nullable=False)
    endereco_id = db.Column(db.Integer, db.ForeignKey('Endereco.id'))
    endereco = db.relationship('Endereco', foreign_keys=[endereco_id])

    # calcula o tamanho dos atributos da pessoa
    def tamanho(self):
        return (sys.getsizeof(self.id) + sys.getsizeof(self.cpf)
         + sys.getsizeof(self.nome) + sys.getsizeof(self.dataNascimento)
         + sys.getsizeof(self.endereco_id) + sys.getsizeof(self.endereco))
        
    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return f"{self.cpf}, {self.nome}, {self.dataNascimento}, {self.endereco}"
