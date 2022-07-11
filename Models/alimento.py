from Config.config import*

import sys
from sys import getsizeof

class Alimento(db.Model):
    __tablename__ = 'Alimento'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    tipo = db.Column(db.String(254))
       
    # método para expressar o professor em forma de texto
    def __str__(self):
        return f"Nome: {self.nome}, Tipo: {self.tipo}"