import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__)) 
parentdir = os.path.dirname(currentdir) 
sys.path.append(parentdir)

from Config.config import *
from Models import *

if os.path.exists(arquivobd):
    os.remove(arquivobd)

# criar tabelas
db.create_all()
