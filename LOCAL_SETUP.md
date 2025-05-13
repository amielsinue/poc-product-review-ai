## 🚀 Running the Project

This project can be run in two different ways: **locally without Docker** or **inside Docker containers**.

---

### 🔧 Option 1: Run without Docker

#### ✅ Requirements

- Python 3.11+
- `virtualenv` or `venv`
- pip

#### 🧪 Steps

```bash
python -m venv venv
source venv/bin/activate
make install
make run
```

The application will be available at: [http://localhost:8000](http://localhost:8000)

---

### 🐳 Option 2: Run with Docker

#### ✅ Requirements

- Docker
- docker-compose

#### 🧪 Steps

```bash
make docker-build
make docker-up
```

Then visit: [http://localhost:8000](http://localhost:8000)

To stop the containers:

```bash
make docker-down
```

---

Both methods will serve the FastAPI app on port `8000`. You can access the interactive API docs at [http://localhost:8000/docs](http://localhost:8000/docs).