# 1. Base Image: Usa una imagen oficial de Python, versión 3.10, más pequeña (slim)
FROM python:3.10-slim

# 2. Variables de Entorno: Configuración estándar para entornos Docker de Python
# Previene la escritura de archivos .pyc
ENV PYTHONDONTWRITEBYTECODE 1
# Asegura que stdout y stderr no estén bufferizados
ENV PYTHONUNBUFFERED 1

# 3. Directorio de Trabajo: Define dónde se ejecutará la aplicación dentro del contenedor
WORKDIR /app

# 4. Instalación de Dependencias: Copia e instala el requirements.txt
# Esto utiliza el caché de Docker de manera eficiente.
# Se asume que tienes un archivo requirements.txt en la raíz de tu repositorio.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copia del Código Fuente: Copia el resto de los archivos del repositorio
# Esto incluye tu app.py y cualquier modelo/archivo de datos (.joblib, .pkl, etc.)
COPY . .

# 6. Puerto: Indica que la aplicación Streamlit escucha en el puerto 8501 (el default)
EXPOSE 8501

# 7. Comando de Ejecución: Define el comando para iniciar la aplicación Streamlit
# Asegúrate de que tu archivo principal sea realmente 'app.py'
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false", "--server.enableXsrfProtection=false"]
