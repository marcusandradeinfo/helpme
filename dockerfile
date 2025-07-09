# Dockerfile
FROM python:3.11-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY . .

# Instala as dependências
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Coleta os arquivos estáticos (mesmo usando SQLite, isso é necessário)
RUN python manage.py collectstatic --noinput

# Expõe a porta do Gunicorn
EXPOSE 8000

# Comando padrão de execução com Gunicorn
CMD ["gunicorn", "app.wsgi:application", "--bind", "0.0.0.0:8000"]