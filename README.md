Crie o arquivo README.md com este conteúdo inicial:

# Granja IoT – Backend

Backend em Django + Django REST Framework para monitoramento remoto
de granjas com sensores e atuadores (IoT).

## Stack
- Python 3.14
- Django 5
- Django REST Framework

## Como executar
```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


Admin:
hgitttp://127.0.0.1:8000/admin

a
*(Depois refinamos)*

---

## 📌 PASSO 6 — Primeiro commit

```powershell
git status


Você deve ver:

manage.py

core/

granja_iot/

README.md

requirements.txt

Agora execute:

git add .
git commit -m "Initial backend - granja IoT"