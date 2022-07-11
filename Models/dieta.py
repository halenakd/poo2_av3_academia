from Config.config import*

import sys
from sys import getsizeof

class Dieta(db.Model):
    __tablename__ = 'Dieta'

    id = db.Column(db.Integer, primary_key=True)
    duracao = db.Column(db.String(254))
    objetivo = db.Column(db.String(254))
    tipo = db.Column(db.String(254))

    # método para expressar o professor em forma de texto
    def __str__(self):
        return f"Duracao: {self.duracao}, Tipo: {self.tipo}, Objetivo: {self.objetivo}"