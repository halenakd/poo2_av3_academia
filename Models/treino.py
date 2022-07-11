from Config.config import *
import sys
from sys import getsizeof

class Treino (db.Model):
    __tablename__ = 'Treino'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo = db.Column(db.String(254))
    vezes = db.Column(db.Integer)
    duracao = db.Column(db.Integer) 
    
    # método para expressar o treino em forma de texto
    def __str__(self):
        return f"Treino: {self.tipo}, {self.vezes} vez(es) p/semana, Duracao: {self.duracao} hora(s)"