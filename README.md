# 📊 API de Predicción con FastAPI y Scikit-learn

Este proyecto implementa un modelo de **Machine Learning** (entrenado en un Jupyter Notebook y guardado como `.pkl`) y lo expone a través de una **API REST con FastAPI**.  
El modelo recibe indicadores económicos como entrada y devuelve una predicción.

---

## 🚀 Características
- Entrenamiento del modelo en Jupyter Notebook (`model.ipynb`).
- Serialización del modelo y del escalador en `.pkl`.
- API en **FastAPI** con endpoint `/predict`.
- Ejemplo de cliente en Python (`example_request.py`) que realiza solicitudes a la API.
- Uso de `joblib` y `scikit-learn` para cargar y ejecutar el modelo.

---

## 📂 Estructura del Proyecto

├── model.ipynb # Notebook donde se entrena el modelo
├── model.pkl # Modelo entrenado (serializado con joblib)
├── scaler.pkl # Escalador usado para normalizar los datos
├── main.py # API con FastAPI
├── example_request.py # Cliente que consume la API
└── README.md # Documentación
