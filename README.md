# 🚀 FastAPI Users CRUD

![Python](https://img.shields.io/badge/python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/framework-FastAPI-green)
![PostgreSQL](https://img.shields.io/badge/database-PostgreSQL-blue)
![Status](https://img.shields.io/badge/status-learning-yellow)

## 📌 Description

**FastAPI Users CRUD** — это простой backend API для управления пользователями.

Проект реализует базовые CRUD операции:

* Create user
* Read users
* Update user
* Delete user

API написан на **FastAPI** и использует **PostgreSQL** в качестве базы данных.

Цель проекта — практика разработки backend сервисов и понимание архитектуры API.

---

# 🧰 Technologies

| Technology   | Purpose          |
| ------------ | ---------------- |
| Python 3.10+ | основной язык    |
| FastAPI      | web framework    |
| PostgreSQL   | база данных      |
| SQLAlchemy   | ORM              |
| Pydantic     | валидация данных |
| Uvicorn      | ASGI сервер      |

---

# ⚙️ Installation

### 1️⃣ Клонировать репозиторий

```bash
git clone https://github.com/arvix-knox/fastapi-users-crud.git
cd fastapi-users-crud
```

---

### 2️⃣ Создать виртуальное окружение

```bash
python -m venv venv
```

---

### 3️⃣ Активировать окружение

Linux / Mac

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

---

### 4️⃣ Установить зависимости

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Настроить переменные окружения

Создай файл `.env`

```env
DATABASE_URL=postgresql://user:password@localhost:5432/fastapi_db
```

---

### 6️⃣ Запустить сервер

```bash
uvicorn main:app --reload
```

---

# 📡 API Endpoints

| Method | Endpoint      | Description                 |
| ------ | ------------- | --------------------------- |
| POST   | `/users`      | создать пользователя        |
| GET    | `/users`      | получить всех пользователей |
| GET    | `/users/{id}` | получить пользователя по id |
| PUT    | `/users/{id}` | обновить пользователя       |
| DELETE | `/users/{id}` | удалить пользователя        |

---

# 🧪 Example Request

### Create User

**POST /users**

Request body

```json
{
  "name": "John"
}
```

Response

```json
{
  "id": 1,
  "name": "John",
  "hobbies": ["reading"]
}
```

---

# 📁 Project Structure

```
fastapi-users-crud
│
├── main.py          # точка входа FastAPI приложения
├── database.py      # подключение к PostgreSQL
├── models.py        # SQLAlchemy модели
├── schemas.py       # Pydantic схемы
├── services.py      # бизнес логика и CRUD операции
│
├── .env             # переменные окружения
├── .gitignore
└── README.md
```

---

# 📖 API Documentation

После запуска сервера документация будет доступна:

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

FastAPI автоматически генерирует OpenAPI документацию.

---

# 📄 License

MIT

---

# 👨‍💻 Author

GitHub:
https://github.com/arvix-knox
