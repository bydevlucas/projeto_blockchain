# Usar uma imagem base do Python
FROM python:3.10

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar o requirements.txt para instalar as dependências
COPY requirements.txt /app/requirements.txt

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código fonte para o container
COPY . /app

# Expor a porta 5000 para o Flask
EXPOSE 5000

# Comando para iniciar a aplicação Flask
CMD ["python", "app/app.py"]
