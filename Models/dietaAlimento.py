from Config.config import*
from Models.alimento import Alimento
from Models.dieta import Dieta

import sys
from sys import getsizeof

class DietaAlimento(db.Model):
    __tablename__ = 'DietaAlimento'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    alimento_id = db.Column(db.Integer, db.ForeignKey('Alimento.id'))
    alimento = db.relationship('Alimento')
    dieta_id = db.Column(db.Integer, db.ForeignKey('Dieta.id'))
    dieta = db.relationship('Dieta')
    qntd = db.Column(db.String(254))
    porcao = db.Column(db.String(254))