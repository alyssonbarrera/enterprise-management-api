FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# CMD ["gunicorn", "--config", "gunicorn.conf.py", "--reload", "app.wsgi:application"]