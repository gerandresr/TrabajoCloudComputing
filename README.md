# 📊 API de Predicción con FastAPI y Scikit-learn

Modelo de Machine Learning que busca predecir el evento de un alza del tipo de cambio USD-CLP para el día siguiente. Este Modelo es una Red Neuronal que se desarrolló por el área de Trading de la Mesa de Dinero de BancoEstado y que actualmente está en uso.

El modelo utiliza como variables independientes diversas medidas macroeconómicas, como Tasas de Interés, Inflación, entre otros.

---

## 🚀 Características
- Entrenamiento del modelo en Jupyter Notebook (`model.ipynb`).
- Serialización del modelo y del escalador en `.pkl`.
- API en **FastAPI**.
- Ejemplo de cliente en Python (`example_request.py`) que realiza solicitudes a la API.
- Uso de `joblib` y `scikit-learn` para cargar y ejecutar el modelo.

---

## 📂 Estructura y Partes del Proyecto

- bd.data_bbg.db: data del proyecto, la base de datos contiene diferentes tablas con informacion diaria de variables financieras.
- data_getters.py: Crea variables categoricas y financieras, se conecta a la base de datos mediante una libreria propia.


- example_request.py # Se conecta a la base de datos

- model.ipynb # Notebook donde se entrena el modelo. Se conecta a 
- model.pkl # Modelo entrenado (serializado con joblib).
- scaler.pkl # Escalador usado para normalizar los datos.
- main.py # API con FastAPI.

- README.md # Documentación.


## Librerias Necesarias

pip install conexion-a-bd.


# Autores
- Gerardo Rios.
- Washington Lizana
