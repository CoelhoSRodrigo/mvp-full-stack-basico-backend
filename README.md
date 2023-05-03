# Meu MVP - Backend

Projeto de MVP do backend do módulo Desenvolvimento Full Stack Básico da especialização online **Pós-Graduação em Desenvolvimento Full Stack**, do Departamento de Informática da PUC-Rio.

Aluno: **Rodrigo dos Santos Coelho** (*https://www.linkedin.com/in/rodrigoscoelho/*)

---
## Primeiros passos

Para executar este projeto é necessário que todas as libs Python descritas no arquivo `requirements.txt` sejam instaladas. 
Após clonar o repositório do GitHub (*https://github.com/CoelhoSRodrigo/mvp-full-stack-basico-backend/*), é necessário ir ao diretório raiz, pelo terminal do Visual Studio Code, para que possa executar os comandos descritos abaixo.

```
python3 -m venv env
```
```
aource env/bin/activate
```

> O primeiro comando iremos utilizar para a criação do ambiente virtual do tipo [virtualenv] e o segundo para ativá-lo(https://virtualenpython -m venv .v.pypa.io/en/latest/).

```
(env)$ pip install -r requirements.txt
```

> O comando acima instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

> O comando acima instala o framework Flask. Pelo fato de estarmos utilizando o parâmetro `--reload`, o servidor web reiniciará automaticamente após uma mudança no código fonte. 
> Caso esteja o utilizando o macOS, pode ser que o AirPlay Receiver já esteja utilizando a portal 5000, sendo assim mude para a portal 5001 o comando do flask caso receba algum alerta do sistema operacional.


Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
