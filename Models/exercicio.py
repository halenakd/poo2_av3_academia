from Config.config import *
import sys
from sys import getsizeof

class Exercicio (db.Model):
    __tablename__ = 'Exercicio'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(254))
    descricao = db.Column(db.String(254))
    series = db.Column(db.Integer)
    repeticoes = db.Column(db.Integer)
    
    # método para expressar o exercicio em forma de texto
    def __str__(self):
        return f"Exercicio: {self.nome}, {self.descricao}, {self.series} series, {self.repeticoes} repeticoes"