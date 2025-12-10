# 📝 Task API — FastAPI + MySQL

Uma API simples e escalável para gerenciamento de tarefas, construída com **FastAPI**, **SQLAlchemy** e banco de dados **MySQL**.
O projeto segue boas práticas de organização e utiliza variáveis de ambiente via **python-dotenv**.

---

## 📦 Tecnologias Utilizadas

* **FastAPI** — Framework moderno e rápido para APIs.
* **Uvicorn** — ASGI server para rodar a aplicação.
* **SQLAlchemy** — ORM para manipulação do banco.
* **PyMySQL** — Conector MySQL.
* **python-dotenv** — Carregamento de variáveis de ambiente.

---

## 📁 Estrutura sugerida do projeto

```
project/
│-- app/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── schemas.py
│   ├── routers/
│   │     └── tasks.py
│   └── ...
│
│-- .env
│-- requirements.txt
│-- README.md
```

---

## ⚙️ Configuração do Ambiente

### 1️⃣ Clone o repositório

```bash
git clone <seu-repositorio>
cd project
```

### 2️⃣ Crie o ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Instale as dependências

O arquivo `requirements.txt` contém:

```
fastapi
uvicorn
sqlalchemy
pymysql
python-dotenv
```

Instale com:

```bash
pip install -r requirements.txt
```

---

## 🗄️ Configuração do Banco de Dados

Crie um banco no MySQL:

```sql
CREATE DATABASE task_api;
```

Configure o arquivo `.env`:

```
DB_USER=root
DB_PASSWORD=suasenha
DB_HOST=localhost
DB_PORT=3306
DB_NAME=task_api
```

---

## 🚀 Executando a Aplicação

```bash
uvicorn app.main:app --reload
```

A API estará disponível em:

➡️ **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

Documentação automática:

* **Swagger UI** → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc** → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📚 Exemplos de Endpoints

### ➕ Criar tarefa (POST /tasks)

```json
{
  "title": "Estudar FastAPI",
  "description": "Ler documentação oficial",
  "completed": false
}
```

### 📋 Listar tarefas (GET /tasks)

### ✔️ Atualizar tarefa (PUT /tasks/{id})

### ❌ Deletar tarefa (DELETE /tasks/{id})

---

## 🧪 Testes

Você pode integrar **pytest** e criar testes para seus endpoints futuramente.

---

## 📄 Licença

Este projeto pode ser utilizado livremente para fins de estudo e desenvolvimento.
