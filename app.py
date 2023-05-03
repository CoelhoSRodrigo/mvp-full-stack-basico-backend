from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from flask_cors import CORS
from models.tarefa import Tarefa
from models import Session
from schemas.tarefa_schema import *
from schemas.error_schema import *

info = Info(title='API MVP PUC-Rio Lojas e-commerce', version='1.0.0')
app = OpenAPI(__name__, info=info)
CORS(app)

tag_tarefa = Tag(name='Tarefa', description='API para operação básica das lojas')


#-------------------------------------
# Definição da documentação do Swagger
#-------------------------------------

@app.route('/',)
def documentacao():
    return redirect('openapi/swagger')


#----------------------------------
# método de requisição POST TAREFA
#----------------------------------
@app.post(
    '/tarefa',
    tags=[tag_tarefa],
    summary='Inclusão de Tarefa.',
    description='Este método permite incluir novas tarefas no banco de dados.',
        responses={
        '201': TarefaSchemaView,
        '400': ErrorSchema 
    }
)
def post_tarefa(form: TarefaSchema):
    session = Session()
    tarefa = Tarefa(
        titulo=form.titulo,
        descricao=form.descricao
    )
    try:
        session.add(tarefa)
        session.commit()
        return apresenta_tarefa(tarefa), 201
    except Exception as e:
        error_msg = e.args
        return {'erro': error_msg}, 400


#---------------------------------
# método de requisição GET TAREFAs
#---------------------------------
@app.get(
    '/tarefas',
    tags=[tag_tarefa],
    summary='Lista de Tarefas.',
    description='Este método retorna todas a tarefas cadastradas.',
    responses={
        '200': TarefaSchemaList,
        '400': ErrorSchema
    }
)
def get_tarefas():
    session = Session()
    tarefas = session.query(Tarefa).all()

    if tarefas:
        return apresenta_tarefas(tarefas), 200
    else:
        error_msg = 'Não existem tarefas cadastradas'
        return {'mesage': error_msg}, 400


#---------------------------------------
# método de requisição TAREFA POR TITULO
#---------------------------------------
@app.get(
    '/tarefaTitulo',
    tags=[tag_tarefa],
    summary='Tarefas por Título',
    description='Este método retorna uma tarefa pelo seu ID.',
    responses={
        '200': TarefaSchemaView,
        '404': ErrorSchema
    }
)
def get_tarefaTitulo(query: TarefaSchemaByTitulo):
    tarefa_titulo = query.titulo
    session = Session()
    tarefas = session.query(Tarefa).filter(Tarefa.titulo.like('%'+tarefa_titulo+'%')).all()
    if tarefas:
        return apresenta_tarefas(tarefas), 200
    else:
        error_msg = 'Tarefa não encontrada'
        return {'mesage': error_msg}, 404


#------------------------------------------
# método de requisição DELETE TAREFA POR ID
#------------------------------------------
@app.delete(
    '/tarefa',
    tags=[tag_tarefa],
    summary='Exclusão de tarefa por ID.',
    description='Este método permite a exclusão de uma tarefa pelo seu ID.',
    responses={
        '200': TarefaSchemaDelete,
        '404': ErrorSchema
    }
)
def delete_tarefa(query: TarefaSchemaById):
    tarefa_id = query.id
    session = Session()

    tarefa = session.query(Tarefa).filter(Tarefa.id == tarefa_id).first()
    
    if tarefa:
        if tarefa.status:
            error_msg = 'Tarefa encerrada não permite exclusão.'
            return {'mesage': error_msg}, 404
        else:
            count = session.query(Tarefa).filter(Tarefa.id == tarefa_id).delete()
            session.commit()
            return {'mesage': 'Tarefa deletada com sucesso', 'id': tarefa_id}, 200
    else:
        print('entrou')
        error_msg = 'Tarefa não encontrada'
        return {'mesage': error_msg}, 404
    
#---------------------------------------
# método de requisição PUT UPDATE STATUS
#---------------------------------------
@app.put(
    '/tarefa',
    tags=[tag_tarefa],
    summary='Alteração do Status por ID.',
    description='Este método permite alterar o status de Tarefas para True.',
    responses={
        '200': TarefaSchemaView,
        '400': ErrorSchema,
        '404': ErrorSchema
    }
)
def update_tarefa(query: TarefaSchemaById, form: TarefaSchemaUpdate):
    session = Session()
    tarefa_id = query.id
    tarefa = session.query(Tarefa).filter(Tarefa.id == tarefa_id).first()

    if tarefa:
        if tarefa.status == False:
            tarefa.status = form.status
            tarefa.atualiza_data_conclusao()
            session.commit()
            return apresenta_tarefa(tarefa), 200
        else:
            error_msg = 'Tarefa já encerrada'
            return {'mesage': error_msg}, 400
    else:
        error_msg = 'Tarefa não encontrada'
        return {'mesage': error_msg}, 404


##############################################################################
# EXECUTAR APLICAÇÃO
##############################################################################
if __name__ == '__main__':
    app.run(debug=True)
