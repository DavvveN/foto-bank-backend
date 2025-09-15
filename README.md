# Foto Bank Backend

This is the backend for the **Foto Bank** app, written in **FastAPI** using **raw SQL** with **MySQL**.  

It supports user creation, querying, and includes unit tests that can be run locally or via GitHub Actions.

---

## Setup

1. **Clone the repository**
```bash
git clone https://github.com/<your-username>/foto-bank-backend.git
cd foto-bank-backend
``` 


2. **Virutal enviorment**
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
``` 

3. **Dependencies**
```bash 
pip install -r requirements.txt
```

4. **Database creation**
```SQL
CREATE DATABASE fotoBankDb;
CREATE DATABASE myappdb_test;  -- for running tests
```

4. **.env file**
```
DB_USER=myuser
DB_PASSWORD=MyNewPassword123!
DB_HOST=localhost
DB_NAME=fotoBankDb
```

5. **.env.test file**
```
DB_USER=myuser
DB_PASSWORD=MyNewPassword123!
DB_HOST=localhost
DB_NAME=myappdb_test
```

6. **Running Backend**
```bash
uvicorn main:app --reload
```

7. **Running tests locally**
```bash 
pytest tests/
``` 