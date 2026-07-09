# Imagen base con Python 3.9
FROM python:3.9

# Define el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de la aplicación al contenedor
COPY . /app

# Da permisos de ejecución al script de particionamiento
RUN chmod +x split_entrada.sh

# Comandos que ejecuta el flujo completo Map -> Reduce
CMD ["bash"]
