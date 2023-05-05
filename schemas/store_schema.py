from pydantic import BaseModel
from typing import List, Optional
from datetime import date, datetime

from sqlalchemy import null
from models.store import Store


class StoreSchema(BaseModel):
    '''Classe que define como uma Store deve ser cadastrada'''
    titulo: str
    descricao: str


class StoreSchemaView(BaseModel):
    '''Classe que define como uma Store cadastrada é apresentada'''
    id: int
    data_criacao: date
    data_conclusao: date
    titulo: str
    descricao: str
    status: bool


class StoreSchemaList(BaseModel):
    '''Define como serão apresentadas todas as Store'''
    stores: List[StoreSchemaView]


class StoreSchemaById(BaseModel):
    '''Define como buscar uma Store pelo ID'''
    id: int


class StoreSchemaByTitulo(BaseModel):
    '''Define como buscar uma Store pelo ID'''
    titulo: str


class StoreSchemaDelete(BaseModel):
    '''Define como uma Store será apresentada após deletada'''
    id: int


class StoreSchemaUpdate(BaseModel):
    '''Este Schema mostra o que deve ser enviado na alteração do status da Store'''
    status: bool


def apresenta_store(store: Store) -> Store:  

    return {
        'id': store.id,
        # 'data_criacao': store.data_criacao.strftime("%d/%m/%Y"),
        'data_criacao': formata_data(store.data_criacao),
        'data_conclusao': formata_data(store.data_conclusao) if store.status == True else store.data_conclusao,
        'titulo': store.titulo,
        'descricao': store.descricao,
        'status': store.status
    }


def apresenta_stores(stores: List[Store]) -> List[Store]:
    storesList = []
    
    for store in stores:

        storesList.append({
            'id': store.id,
            'data_criacao': formata_data(store.data_criacao),
            'data_conclusao': formata_data(store.data_conclusao) if store.status == True else store.data_conclusao,
            'titulo': store.titulo,
            'descricao': store.descricao,
            'status': store.status
        })
    return {'storesList': storesList}


def formata_data(dataBruta: date) -> date:
    '''Função para apresentar a data formatada DD/MM/AAAA'''
    return dataBruta.strftime("%d/%m/%Y")