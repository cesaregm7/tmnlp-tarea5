# Tarea 5

## 1. Prerrequisitos

1. En carpeta raiz del proyecto, se debe crear una carpeta llamada **models**.
2. Crear un ambiente que tenga instalado python 3.
3. Instalar los paquetes de python que se encuentran en el archivo *requirements.txt*

## 2. Instrucciones

1. En la carpeta raiz del proyecto, ejecutar el comando `uvicorn api.main:app --reload` para levantar el servicio.

2. Ingresar al sitio `http://127.0.0.1:8000/docs` y ejecutar el método POST `/train` para generar el modelo.

2. Para ejecutar una predición utilizando el modelo entrenado, utilizar el siguiente endpoint: `http://127.0.0.1:8000/predict?sentences=<sentence>` en donde `sentences` es el parámetro por el cual se le manda una oración y `<sentences>` es el review. Se le puede mandar más de un parámetro `sentences` en el url.

## 3. Ejemplo de uso de endpoint

GET `http://127.0.0.1:8000/predict?sentences=this%20hotel%20was%20awesome`
