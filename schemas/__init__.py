from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.tarefa import Tarefa
import os

# Criação de diretório para a base de dados
db_path = 'database/'

if not os.path.exists(db_path):
    os.makedirs(db_path)

# Define url para criação do banco de dados
db_url = 'sqlite:///%s/base.sqlite3' % db_path

# Criação de Sessão para acesso ao BD
engine = create_engine(db_url, echo=True)

Session = sessionmaker(bind=engine)

# Verifica se banco ainda não existe e cria
if not database_exists(engine.url):
    create_database(engine.url)

# Cria tabelas no banco de dados
Base.metadata.create_all(engine)
