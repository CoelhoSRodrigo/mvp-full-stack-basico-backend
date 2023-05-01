# Meu MVP - Backend

Projeto de MVP do backend do módulo Desenvolvimento Full Stack Básico da especialização online **Pós-Graduação em Desenvolvimento Full Stack**, do Departamento de Informática da PUC-Rio.

Aluno: **Rodrigo dos Santos Coelho** (*https://www.linkedin.com/in/rodrigoscoelho/*)

---
## Primeiros passos

Para executar este projeto é necessário que todas as libs Python descritas no arquivo `appconifg.txt` sejam instaladas. 
Após clonar o repositório do GitHub (*https://github.com/CoelhoSRodrigo/mvp-full-stack-basico-backend/*), é necessário ir ao diretório raiz, pelo terminal do Visual Studio Code, para que possa executar os comandos descritos abaixo.

> Recomendo a utilização de ambiente virtual do tipo [virtualenv](https://virtualenpython -m venv .v.pypa.io/en/latest/).

```
(env)$ pip install -r appconifg.txt
```

> O comando acima instala as dependências/bibliotecas, descritas no arquivo `appconifg.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

> O comando acima instala o framework Flask. Pelo fato de estarmos utilizando o parâmetro `--reload`, o servidor web reiniciará automaticamente após uma mudança no código fonte. 


Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
