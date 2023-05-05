from sqlalchemy import Column, Integer, String, Boolean, Date
from datetime import date
from models.base import Base


class Store(Base):
    __tablename__ = 'store'
    '''Definição dos campos da nova tabela Store'''

    id = Column('pk_store', Integer, primary_key=True)
    data_criacao = Column(Date, default=date.today)
    data_conclusao = Column(Date, nullable=True)
    titulo = Column(String(100), nullable=False)
    descricao = Column(String(1000), nullable=False)
    status = Column(Boolean, default=False)


    '''Função construtora da classe Store'''
    def __init__(self, titulo: str, descricao: str) -> None:
        self.titulo = titulo
        self.descricao = descricao


    '''Função utilizada sempre que uma Store for encerrada, para gravar a data'''
    def atualiza_data_conclusao(self) -> None:
        self.data_conclusao = date.today()
