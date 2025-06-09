# Usa uma imagem leve do Python
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY . .

# Instala as dependências da aplicação
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta onde a API vai rodar
EXPOSE 1313

# Comando para rodar a API
CMD ["python", "app.py"]