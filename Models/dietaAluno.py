from Config.config import *
from Models.aluno import Aluno
from Models.dieta import Dieta

import sys
from sys import getsizeof

class DietaAluno(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dieta_id = db.Column(db.Integer, db.ForeignKey('Dieta.id'), nullable=False)
    dieta = db.relationship('Dieta')
    aluno_id = db.Column(db.String(11), db.ForeignKey('Aluno.id'), nullable=False)
    aluno = db.relationship('Aluno')
    data_inicio = db.Column(db.Date(), nullable=False)