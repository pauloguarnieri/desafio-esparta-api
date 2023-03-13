# desafio-esparta-api

---
### Faça um clone do repositorio: 
```
git clone git@github.com:pauloguarnieri/desafio-esparta-api.git
```
###  Crie seu ambiente virtual:

```shell
python -m venv venv
```

###  Ative seu venv:

```shell
# linux:
source venv/bin/activate

# windows:
.\venv\Scripts\activate
```

###  Instale as dependencias do projeto:

```
pip install -r requirements.txt
```

###  Gerar banco de dados SQLITE:

```
python manage.py migrate
```

###  Rodar a aplicação

```
python manage.py runserver
```
---
### Endpoints

Uma documentação Swagger pode ser encontrada no endoint:
 api/docs/
 ela detalha sobre cada endpoint citado abaixo.

- Project
  - POST - api/project/  -   (criação de um projeto)
  - GET - api/project/  -  (listagem dos projetos existentes)
  - GET - api/project/:project_id/  -  (exibe um projeto especifico)
  - PATCH - api/project/:project_id/  -  (update de um projeto)
  - DELETE - api/project/:project_id/  -  (deleção de um projeto)
- Task
  - POST - api/task/project/:project_id/  -  (cria uma task em determinado projeto)
  - GET - api/task/project/:project_id/  -  (lista todas tasks de determinado projeto)
  - GET - api/task/:task_id/  -  (exibe uma task espeficica)
  - PATCH - api/task/:task_id/  -  (update de uma task)
  - DELETE - api/task/:task_id/  -  (deleção de uma task)

---

### DER e WORKSPACE

```
Dentro do projeto tem uma pasta 'assets' onde deixei o DER e 
um workspace que criei para testar as rotas (convertido em JSON);
```
---
### Tecnologias utilizadas:
```
- [Django](https://docs.djangoproject.com/)
- [Rest_Framework](https://www.django-rest-framework.org/)
- [SQLite](https://www.sqlite.org/index.html/)
```