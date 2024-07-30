FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt
COPY app.py app.py
COPY metrics.py metrics.py
COPY gunicorn.conf.py gunicorn.conf.py
COPY static static
COPY templates templates

RUN pip install gunicorn
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "app:app"]
