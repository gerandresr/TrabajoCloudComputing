# 📊 API de Predicción del USDCLP con FastAPI y MachineLearning

Modelo de Machine Learning que busca predecir el evento alzas/bajas del tipo de cambio USD-CLP basado en los datos de cierre del día anterior. Este Modelo es una Red Neuronal que se desarrolló por el área de Trading de la Mesa de Dinero de BancoEstado y que actualmente está en uso.

El modelo utiliza como variables independientes, diversas medidas macroeconómicas; como Tasas de Interés, Inflación, Commodities, Equity, entre otros.

---

# 👥 Autores
- Gerardo Rios.
- Washington Lizana.

---

## 📂 Estructura y Partes del Proyecto

### Ejecucion y explicación del Poyecto:
- Informe.pdf: Documentacion detallada del poyecto y screenshots de funcionamiento corriendo Localmente.
### Archivos necesarios:
- bd.data_bbg.db: Data del proyecto, la base de datos contiene diferentes tablas con informacion diaria de variables financieras.
- data_getters.py: Crea variables categoricas y financieras, se conecta a la base de datos mediante una libreria propia.
- model.ipynb: Notebook donde se entrenan el modelos y se elige el "Mejor"
- model.pkl: Modelo entrenado (serializado con joblib). Creado en Notebook Model.
- scaler.pkl: Escalador usado para normalizar los datos. Creado en Notebook Model.
- main.py: API con FastAPI.
### Otros:
- saca_datos_bbg_a_db.py: En caso de tener una suscripcion activa a Bloomberg Anywhere (https://www.bloomberg.com/), puedes sacar data actualizada.
- example_database.ipynb: Notebook con ejemplo de como ocupar la base de datos usando la libreria propia.
- example_request.py: Ejemplo de como conectarse a la API.
- requirements.txt: Librerias necesarias
- README.md: Documentación.
  
---

## ⚙️ Librerias Necesarias
- Libreria propia "conexion-a-db" se recomenda instalar individualmente. "pip install conexion-a-db". https://pypi.org/project/conexion-a-db/
- Otras librerias se pueden instalar directamente con requirements.txt

---

## 🤖 Como correr Proyecto de ML y FastAPI

- Guardar todos los archivos en una misma carpeta
- correr model.ipynb, el cual generara 2 archivos .pkl con del modelo
- generar la api con fast api:
- En la terminal escribir "fastapi dev main.py"
- Ejecutar api, como por ejemplo con example_request.py, para esto:
-> Abrir nueva terminal y escribir "python example_request.py"
