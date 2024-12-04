# Usa una imagen base oficial de Python
FROM python:3.12-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos Pipfile y Pipfile.lock al contenedor
COPY Pipfile Pipfile.lock /app/

# Instala pipenv y las dependencias
RUN pip install pipenv && pipenv install --deploy --system

# Copia el código de la aplicación al contenedor
COPY . /app

# Expone el puerto 5000 para Flask
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
