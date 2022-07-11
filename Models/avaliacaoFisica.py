from Config.config import *
from Models.aluno import Aluno

import sys
from sys import getsizeof

class AvaliacaoFisica(db.Model):
    __tablename__ = 'AvaliacaoFisica'

    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.String(254), db.ForeignKey('Aluno.id', ondelete="CASCADE"))
    aluno = db.relationship("Aluno")
    data = db.Column(db.Date(), nullable=False)
    peso = db.Column(db.Integer)
    altura = db.Column(db.Integer)
    imc = db.Column(db.Integer)
    med_abdn = db.Column(db.Integer)       

# método para expressar o professor em forma de texto
    def __str__(self):
        return f"Avaliacao Fisica: Aluno: {self.aluno.nome}, Peso: {self.peso}, Altura: {self.altura}, IMC: {self.imc}, Medida do Abdomen: {self.med_abdn}"
    
