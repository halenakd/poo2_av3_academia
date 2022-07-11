from Config.config import *
from Models.colaborador import Colaborador
import sys
from sys import getsizeof

class Professor(Colaborador):
    __tablename__ = 'Professor'
    
    id = db.Column(db.Integer, db.ForeignKey('colaborador.id', ondelete="CASCADE"), primary_key=True)
    # lista reversa!
    alunos = db.relationship('Aluno', backref='professor')

    # método para expressar o professor em forma de texto
    def __str__(self):
        return f"Professor: {self.nome}, Turno: {self.turno}, Salário: {self.salario}"