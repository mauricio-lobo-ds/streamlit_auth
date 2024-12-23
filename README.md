# Streamlit Authenticator Project

Este projeto é uma aplicação de autenticação usando Streamlit e PostgreSQL. Ele permite que os usuários façam login, se registrem e gerenciem suas sessões de forma segura.

## Estrutura do Projeto

```
project/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── auth.py
│   ├── forms.py
│   └── views.py
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── database/
│   ├── __init__.py
│   ├── connection.py
│   ├── queries.py
│   └── db_interface.py
│
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
└── venv/
```

## Configuração do Ambiente

1. Renomeie o arquivo `.env.example` para `.env`.

2. Preencha as variáveis de ambiente no arquivo `.env` com as informações apropriadas.

```properties
# Nome do banco de dados
DATABASE='your_database_name'

# Host do banco de dados
HOST='your_database_host'

# Usuário do servidor de banco de dados
USERSERVER='your_database_user'

# Senha do servidor de banco de dados
PASSWORD='your_database_password'

# Porta do banco de dados
PORT='your_database_port'
```

## Instalação

1. Crie e ative um ambiente virtual:

```sh
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
```

2. Instale as dependências:

```sh
pip install -r requirements.txt
```

## Executando a Aplicação

Para iniciar a aplicação, execute o seguinte comando:

```sh
streamlit run app/main.py
```

## Estrutura dos Arquivos

### `app/`

- `main.py`: Ponto de entrada principal da aplicação.
- `auth.py`: Lógica de autenticação.
- `forms.py`: Formulários de login e registro.
- `views.py`: Lógica principal da aplicação.

### `config/`

- `settings.py`: Configurações do projeto, como variáveis de ambiente.

### `database/`

- `connection.py`: Conexão com o banco de dados.
- `queries.py`: Funções de consulta ao banco de dados.
- `db_interface.py`: Interface de banco de dados para facilitar a troca de SGBD.

