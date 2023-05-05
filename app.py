from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from flask_cors import CORS
from models.store import Store
from models import Session
from schemas.store_schema import *
from schemas.error_schema import *

info = Info(title='MVP PUC-Rio Lojas e-Commerce', version='1.0.0')
app = OpenAPI(__name__, info=info)
CORS(app)

tag_store = Tag(name='Store', description='API para operação básica das lojas')


#-------------------------------------
# Definição da documentação do Swagger
#-------------------------------------
@app.route('/',)
def documentacao():
    return redirect('openapi/swagger')


#----------------------------------
# método de requisição POST Store
#----------------------------------
@app.post(
    '/store',
    tags=[tag_store],
    summary='Criando uma loja.',
    description='Método responsável pela criação de uma loja no banco de dados.',
        responses={
        '201': StoreSchemaView,
        '400': ErrorSchema 
    }
)
def post_store(form: StoreSchema):
    session = Session()
    store = Store(
        titulo=form.titulo,
        descricao=form.descricao
    )
    try:
        session.add(store)
        session.commit()
        return apresenta_store(store), 201
    except Exception as e:
        error_msg = e.args
        return {'erro': error_msg}, 400


#---------------------------------
# método de requisição GET Stores
#---------------------------------
@app.get(
    '/stores',
    tags=[tag_store],
    summary='Todas as lojas.',
    description='Método responsável por retonar todas as lojas de e-coomerce criadas.',
    responses={
        '200': StoreSchemaList,
        '400': ErrorSchema
    }
)
def get_stores():
    session = Session()
    stores = session.query(Store).all()

    if stores:
        return apresenta_stores(stores), 200
    else:
        error_msg = 'Não existem stores cadastradas'
        return {'mesage': error_msg}, 400


#---------------------------------------
# método de requisição store POR TITULO
#---------------------------------------
@app.get(
    '/storeTitulo',
    tags=[tag_store],
    summary='Stores por Título',
    description='Este método retorna uma store pelo seu ID.',
    responses={
        '200': StoreSchemaView,
        '404': ErrorSchema
    }
)
def get_storeTitulo(query: StoreSchemaByTitulo):
    store_titulo = query.titulo
    session = Session()
    stores = session.query(Store).filter(Store.titulo.like('%'+store_titulo+'%')).all()
    if stores:
        return apresenta_stores(stores), 200
    else:
        error_msg = 'Store não encontrada'
        return {'mesage': error_msg}, 404


#------------------------------------------
# método de requisição DELETE Store POR ID
#------------------------------------------
@app.delete(
    '/store',
    tags=[tag_store],
    summary='Exclusão de store por ID.',
    description='Este método permite a exclusão de uma store pelo seu ID.',
    responses={
        '200': StoreSchemaDelete,
        '404': ErrorSchema
    }
)
def delete_store(query: StoreSchemaById):
    store_id = query.id
    session = Session()

    store = session.query(Store).filter(Store.id == store_id).first()
    
    if store:
        if store.status:
            error_msg = 'Sorry! Não é permitido a remoção da loja com status encerrada.'
            return {'mesage': error_msg}, 404
        else:
            count = session.query(Store).filter(Store.id == store_id).delete()
            session.commit()
            return {'mesage': 'Loja removida com sucesso', 'id': store_id}, 200
    else:
        print('entrou')
        error_msg = 'Ops! Loja não localizada'
        return {'mesage': error_msg}, 404
    
#---------------------------------------
# método de requisição PUT UPDATE STATUS
#---------------------------------------
@app.put(
    '/store',
    tags=[tag_store],
    summary='Alteração do Status por ID.',
    description='Este método permite alterar o status de Stores para True.',
    responses={
        '200': StoreSchemaView,
        '400': ErrorSchema,
        '404': ErrorSchema
    }
)
def update_store(query: StoreSchemaById, form: StoreSchemaUpdate):
    session = Session()
    store_id = query.id
    store = session.query(Store).filter(Store.id == store_id).first()

    if store:
        if store.status == False:
            store.status = form.status
            store.atualiza_data_conclusao()
            session.commit()
            return apresenta_store(store), 200
        else:
            error_msg = 'Store já encerrada'
            return {'mesage': error_msg}, 400
    else:
        error_msg = 'Store não encontrada'
        return {'mesage': error_msg}, 404


##############################################################################
# EXECUTAR APLICAÇÃO
##############################################################################
if __name__ == '__main__':
    app.run(debug=True)
