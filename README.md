<h1 align="center">NLW Journey - API Gerenciamento de Viagens</h1>

<p align="center">
  <img alt="Flask" src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white"/>
  <img alt="Python" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>
  <img alt="SQLAlchemy" src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white"/>
  <img alt="SQLite" src="https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white"/>
  <img alt="Pytest" src="https://img.shields.io/badge/pytest-%23ffffff.svg?style=for-the-badge&logo=pytest&logoColor=black"/>
</p>

<p align="center">
  <a href="#-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-principais-bibliotecas">Principais Bibliotecas</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-como-executar">Como Executar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-endpoints">Endpoints</a>
</p>

## 🚀 Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

- **Python** - Linguagem de programação principal
- **Flask** - Framework web minimalista para Python
- **SQLAlchemy** - ORM para manipulação do banco de dados
- **SQLite** - Banco de dados leve e eficiente
- **Pytest** - Framework para testes automatizados
- **UUID** - Para geração de identificadores únicos

## 📚 Principais Bibliotecas

- **Flask** - Framework principal para criação da API REST
- **Flask-SQLAlchemy** - Extensão que adiciona suporte ao SQLAlchemy no Flask
- **Werkzeug** - Biblioteca de utilitários WSGI
- **Pytest** - Para criação e execução de testes automatizados
- **Datetime** - Para manipulação de datas e horários

## 💻 Projeto

Esta é uma **API RESTful de gerenciamento de viagens** desenvolvida com Flask durante o NLW Journey da Rocketseat. O é um sistema completo para planejamento de viagens colaborativas, permitindo organizar roteiros, atividades e links úteis com amigos.

A aplicação oferece funcionalidades essenciais para planejamento de viagens:

- **Criação de viagens** com destino, datas e participantes
- **Gerenciamento de participantes** com sistema de convites
- **Confirmação de viagens** e participantes
- **Cadastro de atividades** com data e horário específicos
- **Organização de links úteis** para a viagem
- **Validação de datas** e consistência de dados
- **Sistema de notificações** para participantes

O projeto segue as melhores práticas de desenvolvimento, incluindo estruturação de código modular, validação de dados, tratamento de erros e implementação de testes automatizados.

## 🔧 Como Executar

### Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes do Python)
- Git

### 1. Clone o repositório
```bash
git clone https://github.com/davioliveiraes/nlw-python-journey.git
cd nlw-python-journey
```

### 2. Crie e ative o ambiente virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados
```bash
# Execute o Python para criar as tabelas
python
>>> from src.main.server.server import app
>>> from src.models.settings.db_connection_handler import db_connection_handler
>>> with app.app_context():
...     db_connection_handler.get_engine().create_all()
>>> exit()
```

### 5. Execute a aplicação
```bash
python run.py
```

A API estará disponível em `http://127.0.0.1:3000`

### 6. Para executar os testes
```bash
# Execute todos os testes
pytest

# Execute testes com verbosidade
pytest -v

# Execute testes de cobertura
pytest --cov
```

## 🛣️ Endpoints

### Viagens (Trips)
| Método | Endpoint | Descrição | Autenticação |
|--------|----------|-----------|--------------|
| `POST` | `/trips` | Cria uma nova viagem | ❌ |
| `GET` | `/trips/<:tripId>` | Busca detalhes de uma viagem | ❌ |
| `PUT` | `/trips/<:tripId>` | Confirma uma viagem | ❌ |

### Participantes (Participants)
| Método | Endpoint | Descrição | Autenticação |
|--------|----------|-----------|--------------|
| `POST` | `/trips/<:tripId>/invites` | Cria convite para participante | ❌ |
| `GET` | `/trips/<:tripId>/participants` | Lista participantes da viagem | ❌ |
| `GET` | `/participants/<:participantId>` | Busca detalhes de um participante | ❌ |
| `PATCH` | `/participants/<:participantId>/confirm` | Confirma participação na viagem | ❌ |

### Atividades (Activities)
| Método | Endpoint | Descrição | Autenticação |
|--------|----------|-----------|--------------|
| `POST` | `/trips/<:tripId>/activities` | Cria uma nova atividade | ❌ |
| `GET` | `/trips/<:tripId>/activities` | Lista atividades da viagem | ❌ |

### Links
| Método | Endpoint | Descrição | Autenticação |
|--------|----------|-----------|--------------|
| `POST` | `/trips/<:tripId>/links` | Cria um novo link útil | ❌ |
| `GET` | `/trips/<:tripId>/links` | Lista links da viagem | ❌ |

### Exemplos de Uso

#### Criar viagem
```json
POST /trips
{
  "destination": "Rio de Janeiro, RJ",
  "starts_at": "2024-08-01T10:00:00",
  "ends_at": "2024-08-05T18:00:00",
  "owner_name": "João Silva",
  "owner_email": "joao@email.com",
  "emails_to_invite": [
    "maria@email.com",
    "pedro@email.com"
  ]
}
```

#### Resposta
```json
{
  "tripId": "f944daf7-e7e6-47a2-b050-1556d6a9e963"
}
```

#### Buscar viagem
```json
GET /trips/f944daf7-e7e6-47a2-b050-1556d6a9e963

{
  "trip": {
    "id": "f944daf7-e7e6-47a2-b050-1556d6a9e963",
    "destination": "Rio de Janeiro, RJ",
    "starts_at": "2024-08-01T10:00:00",
    "ends_at": "2024-08-05T18:00:00",
    "is_confirmed": 1
}
```

#### Criar atividade
```json
POST /trips/f944daf7-e7e6-47a2-b050-1556d6a9e963/activities
{
  "title": "Visita ao Cristo Redentor",
  "occurs_at": "2024-08-02T14:00:00"
}
```

#### Criar link útil
```json
POST /trips/f944daf7-e7e6-47a2-b050-1556d6a9e963/links
{
  "title": "Roteiro Turístico RJ",
  "url": "https://www.visitrio.com.br"
}
```

## 🔄 Fluxo da Aplicação

1. **Criação da viagem**: Usuário cria uma viagem informando destino, datas e emails dos convidados
2. **Convites automáticos**: Sistema envia convites para os participantes via email
3. **Confirmação**: Organizador confirma a viagem após receber as confirmações
4. **Planejamento**: Participantes podem adicionar atividades e links úteis
5. **Execução**: Durante a viagem, atividades podem ser marcadas como realizadas

## 🧪 Testes

O projeto inclui uma suíte completa de testes automatizados:

- **Testes unitários** para modelos e validações
- **Testes de integração** para endpoints da API
- **Testes de validação** para entrada de dados
- **Cobertura de código** para garantir qualidade

```bash
# Executar testes específicos
pytest -s -v src/models/repositories/trips_repository_test.py
pytest -s -v src/models/repositories/participants_repository_test.py
pytest -s -v src/models/repositories/links_repository_test.py
pytest -s -v src/models/repositories/emails_to_invite_repository_test.py
pytest -s -v src/models/repositories/activities_repository_test.py
```

## 📁 Estrutura do Projeto

```
nlw-python-journey/
├── .vscode/
├── init/
├── src/
│   ├── controllers/
│   ├── drivers/
│   ├── main/
│   │    ├── routes/
│   │    ├── server/
│   ├── models/
│   │    ├── repositories/
│   │    ├── settings/
├── create_email.py
├── README.md
├── requirements.txt
├── run.py
└── storage.db
```

<p align="center">Desenvolvido no evento NLW Journey da Rocketseat 🚀</p>