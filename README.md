# 📊 API de Predicción con FastAPI y Scikit-learn

Modelo de Machine Learning que busca predecir el evento de un alza del tipo de cambio USD-CLP para el día siguiente. Este Modelo es una Red Neuronal que se desarrolló por el área de Trading de la Mesa de Dinero de BancoEstado y que actualmente está en uso.

El modelo utiliza como variables independientes diversas medidas macroeconómicas, como Tasas de Interés, Inflación, entre otros.

---

## 🚀 Características
- Entrenamiento del modelo en Jupyter Notebook (`model.ipynb`).
- Serialización del modelo y del escalador en `.pkl`.
- API en **FastAPI** con endpoint `/predict`.
- Ejemplo de cliente en Python (`example_request.py`) que realiza solicitudes a la API.
- Uso de `joblib` y `scikit-learn` para cargar y ejecutar el modelo.

---

## 📂 Estructura del Proyecto

- model.ipynb # Notebook donde se entrena el modelo.
- model.pkl # Modelo entrenado (serializado con joblib).
- scaler.pkl # Escalador usado para normalizar los datos.
- main.py # API con FastAPI.
- example_request.py # Cliente que consume la API.
- README.md # Documentación.
