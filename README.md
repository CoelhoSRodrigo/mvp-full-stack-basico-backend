# API TAREFA
Esta API foi desenvolvida para entrega do MVP da Sprint 1 da PUC-RIO. Ela foi desenvolvida em Flask para servir uma aplicação
desenvolvida em HTML, CSS e JS.

### Esta API trás os seguintes métodos:

| Método           | Funcionalidade                            |
|------------------|-------------------------------------------|
| DELETE/tarefa    | Deleta uma tarefa por ID                  |
| POST/tarefa      | Cadastra uma nova tarefa                  |
| PUT/tarefa       | Atualiza o Status de uma tarefa existente |
| GET/tarefaTitulo | Busca tarefas pelo Título                 |
| GET/tarefas      | Busca todas as tarefas                    |

# Como executar

Você precisa ter todas as libs utilizadas no projeto e que estão listadas no arquivo requirements.txt.

Para executar este projeto você poderá criar um ambiente virtual primeiramente e ativá-lo. No linux, 
onde desenvolvi o projeto, na linha de comando na raiz do projeto, utilizo o comando:

```
python3 -m venv env
```

Após criar o ambiente virtual de nov env, estando ainda na raiz do projeto, ativar:
```
source env/bin/activate
```

Quando a virtual env estiver ativa, irá aparecer antes do caminho do projeto no cmd o nome (env). Agora, é necessário instalar as libs:
```
pip install -r requirements.txt
```

Para executar, se estiver utilizando o VSCode, abra o arquivo APP.py e utilize o atalho CTRL+F5 ou se estiver utilizando outro IDE de desenvolvimento
procure nas opções do menu a opção de executar/rodar. Em seguida, abra o seu navegador e cole o endereço da API para ver a documentação:
```
http://127.0.0.1:5000/
```

Esta página permitirá explorar a documentação da API

### Para instalar e ativar a virtual env no windows:

No windows, na raiz do projeto, exexute:
```
python -m venv env
```

Para ativar a env, execute:
```
env/Scripts/activate
```