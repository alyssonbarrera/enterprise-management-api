bind = '0.0.0.0:8000'  # Endereço IP e porta onde o servidor Gunicorn deve ser executado
workers = 4  # Número de processos de trabalhador para Gunicorn iniciar
timeout = 120  # Tempo limite (em segundos) para o Gunicorn responder a uma solicitação HTTP
max_requests = 1000  # Número máximo de solicitações HTTP por trabalhador antes de ser reiniciado
preload_app = True  # Ativa a carga antecipada do aplicativo para reduzir o tempo de inicialização

app_path = 'app.wsgi:application'
