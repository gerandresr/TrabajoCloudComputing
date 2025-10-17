# 📊 API de Predicción con FastAPI y Scikit-learn

Modelo de Machine Learning que busca predecir el evento de un alza del tipo de cambio USD-CLP para el día siguiente. Este Modelo es una Red Neuronal que se desarrolló por el área de Trading de la Mesa de Dinero de BancoEstado y que actualmente está en uso.

El modelo utiliza como variables independientes diversas medidas macroeconómicas, como Tasas de Interés, Inflación, entre otros.

---

# Autores
- Gerardo Rios.
- Washington Lizana

---

## 📂 Estructura y Partes del Proyecto

- Informe.pdf: Documentacion detallada del poyecto y screenshots de funcionamientos Local.

- bd.data_bbg.db: data del proyecto, la base de datos contiene diferentes tablas con informacion diaria de variables financieras.
- data_getters.py: Crea variables categoricas y financieras, se conecta a la base de datos mediante una libreria propia.
- model.ipynb: Notebook donde se entrenan el modelos y se elige el "Mejor"
- model.pkl: Modelo entrenado (serializado con joblib). Creado en Notebook Model.
- scaler.pkl: Escalador usado para normalizar los datos. Creado en Notebook Model.
- main.py: API con FastAPI.

### Otros:
- saca_datos_bbg_a_db.py: En caso de tener una suscripcion activa a Bloomberg, puedes sacar data actualizada.
- example_database.ipynb: Notebook con ejemplo de como ocupar la base de datos usando la libreria propia.
- example_request.py # Ejemplo de como conectarse a la API.
- README.md # Documentación.
---
## Librerias Necesarias

pip install conexion-a-bd.

## Como correr Proyecto


