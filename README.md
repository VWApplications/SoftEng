# SoftEng

Ontologia do curso de Engenharia de Software

#### Como acessar a aplicação localmente:

1. De um clone do repositório da aplicação ```https://github.com/VictorArnaud/SoftEng.git```

2. Instale as dependencias para rodar o python3 e pip3

```
sudo apt-get update
sudo apt-get install -y python3-dev sqlite python3-pip libpq-dev
```

3. Criar o ambiente virtual de desenvolvimento (virtualenvwrapper)

```
sudo pip3 install --upgrade pip
sudo pip3 install virtualenvwrapper
```

4. No arquivo .bashrc do link insira:

```
WORKON_HOME=~/.virtualenvs
VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
```

* Para criar um ambiente virtual: ```mkvirtualenv <venv_name>```

* Para entrar no ambiente virtual: ```workon <venv_name>```

* Para sair do ambiente virtual: ```deactivate```

5. Instalar o software e o banco de triplas

```
make
```

6. Crie o repositorio do banco de triplas

```
Navegador: http://localhost:8001/openrdf-workbench/
```

* Dentro do banco de triplas no navegador crie um novo repositorio chamado **softeng** e aperte next duas vezes no banco de triplas

![img1](https://user-images.githubusercontent.com/14116020/41176876-6dcba296-6b38-11e8-988f-e9e5a2bd3329.png)

* Execute o comando para popular o banco de triplas

```
make populate
```

7. Rode a aplicação


```
make run
Navegador: http://0.0.0.0:8000/
```

#### API

```
Executar query: http://0.0.0.0:8000/api/
Criar e listar queries: http://0.0.0.0:8000/api/queries/
Editar e deletar queries: http://0.0.0.0:8000/api/queries/<query_id>/details/
```
