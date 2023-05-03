from pydantic import BaseModel
from typing import List, Optional
from datetime import date, datetime

from sqlalchemy import null
from models.tarefa import Tarefa


class TarefaSchema(BaseModel):
    '''Classe que define como uma tarefa deve ser cadastrada'''
    titulo: str
    descricao: str


class TarefaSchemaView(BaseModel):
    '''Classe que define como uma tarefa cadastrada é apresentada'''
    id: int
    data_criacao: date
    data_conclusao: date
    titulo: str
    descricao: str
    status: bool


class TarefaSchemaList(BaseModel):
    '''Define como serão apresentadas todas as tarefas'''
    tarefas: List[TarefaSchemaView]


class TarefaSchemaById(BaseModel):
    '''Define como buscar uma tarefa pelo ID'''
    id: int


class TarefaSchemaByTitulo(BaseModel):
    '''Define como buscar uma tarefa pelo ID'''
    titulo: str


class TarefaSchemaDelete(BaseModel):
    '''Define como uma tarefa será apresentada após deletada'''
    id: int


class TarefaSchemaUpdate(BaseModel):
    '''Este Schema mostra o que deve ser enviado na alteração do status da Tarefa'''
    status: bool


def apresenta_tarefa(tarefa: Tarefa) -> Tarefa:  

    return {
        'id': tarefa.id,
        # 'data_criacao': tarefa.data_criacao.strftime("%d/%m/%Y"),
        'data_criacao': formata_data(tarefa.data_criacao),
        'data_conclusao': formata_data(tarefa.data_conclusao) if tarefa.status == True else tarefa.data_conclusao,
        'titulo': tarefa.titulo,
        'descricao': tarefa.descricao,
        'status': tarefa.status
    }


def apresenta_tarefas(tarefas: List[Tarefa]) -> List[Tarefa]:
    tarefasList = []
    
    for tarefa in tarefas:

        tarefasList.append({
            'id': tarefa.id,
            'data_criacao': formata_data(tarefa.data_criacao),
            'data_conclusao': formata_data(tarefa.data_conclusao) if tarefa.status == True else tarefa.data_conclusao,
            'titulo': tarefa.titulo,
            'descricao': tarefa.descricao,
            'status': tarefa.status
        })
    return {'tarefasList': tarefasList}


def formata_data(dataBruta: date) -> date:
    '''Função para apresentar a data formatada DD/MM/AAAA'''
    return dataBruta.strftime("%d/%m/%Y")