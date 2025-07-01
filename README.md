# Backend do MVP Musculação_App

Este é o backend do MVP do aplicativo Musculação_App, desenvolvido para auxiliar no acompanhamento de treinos de musculação. O projeto foi criado utilizando Python e Flask.

## Como executar 

### Passo 1: Instalação do Python

Instale o Python versão 3.13.2.

É necessário ir ao diretório raiz dessa aplicação, pelo terminal, para poder executar os comandos descritos abaixo.

### Passo 2 (opcional): Instalação do Ambiente Virtual

Recomenda-se utilizar o ambiente virtual: [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)

Para isso, no terminal, dentro da pasta da api, digite:
```
python -m venv .venv
```

Isso irá criar um ambiente virtual chamado `.venv`.

Talvez seja necessário antes alterar a política de execução do PowerShell para permitir a execução de scripts. Para isso, execute o seguinte comando no PowerShell:
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Em seguida, digite o comando abaixo para ativar o ambiente virtual:
```
.\.venv\Scripts\activate
```
Isso irá ativar o ambiente virtual, e você verá o prefixo `(venv)` no terminal, indicando que o ambiente está ativo.

### Passo 3: Instalação das Dependências

Execute o seguinte comando:
```
(env)$ pip install -r requirements.txt
```
Isso irá instalar as bibliotecas contidas no arquivo `requirements.txt`.

### Passo 4: Executar a API

Execute o seguinte comando:
```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar a API em execução.
