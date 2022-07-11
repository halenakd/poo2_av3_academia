from Config.config import *
from Models.usuario import Usuario
from Models.professor import Professor
from Models.treino import Treino
import sys
from sys import getsizeof


class Aluno(Usuario):
    __tablename__ = 'Aluno'

    id = db.Column(db.Integer, db.ForeignKey('usuario.id', ondelete="CASCADE"), primary_key=True)
    prof_id = db.Column(db.String(11), db.ForeignKey('Professor.id', ondelete="CASCADE"))
    treino_id = db.Column(db.ForeignKey('Treino.id'))
    treino = db.relationship("Treino", foreign_keys=[treino_id])   
    objetivo = db.Column(db.String(254))
    
    # calcula o tamanho dos atributos do aluno e soma com os do usuario
    def tamanho(self):
        return (sys.getsizeof(self.id) + sys.getsizeof(self.prof_id) 
                + sys.getsizeof(self.treino_id)
                + sys.getsizeof(self.objetivo) + super().tamanho())

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return f"Aluno: {self.nome}, Endereco: {str(self.endereco)},\nProfessor: {self.professor.nome}, Treino {self.treino.tipo}, Objetivo: {self.objetivo}"