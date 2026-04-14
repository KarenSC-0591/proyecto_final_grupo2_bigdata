Proyecto Final - Análisis de Datos Grupo 2 (Big Data)
Integrantes
Karen Sánchez 
Raúl 
Byron 
Joel 
Rommer 

Descripción

Este proyecto consiste en el desarrollo de una plataforma en Python para el análisis y validación de datos, dividida en dos módulos principales:

Proyecto 2: Sistema de Monitoreo de Ventas
Proyecto 3: Data Quality Checker

El sistema permite cargar datasets en formato CSV, analizarlos, generar visualizaciones y validar la calidad de los datos.

Características
Lectura de datos con pandas
Análisis de ventas (totales y agrupaciones)
Visualización de datos con matplotlib
Validación de calidad de datos:
Valores nulos
Duplicados
Tipos de datos
Generación de reportes automáticos
Arquitectura

El proyecto está dividido en dos módulos independientes dentro del mismo repositorio:

sales_monitoring/ → Análisis de ventas
data_quality_checker/ → Validación de datos

Cada módulo sigue una arquitectura modular basada en:

Carga de datos
Procesamiento
Salida (output)
📁 Estructura del Proyecto
PROYECTO_FINAL_GRUPO2_BIGDATA/

├── data_quality_checker/
│   ├── data/
│   │   └── proyecto3_empleados.csv
│   ├
│   ├── outputs/
│   │   └── errors.txt
│   ├── src/
│   │   ├── load_data.py
│   │   ├── validation.py
│   │   └── report.py
│
├── sales_monitoring/
│   ├── data/
│   │   └── proyecto2_ventas.csv
│   ├── output/
│   ├── src/
│   │   ├── load_data.py
│   │   └── visualization.py
│
├── main.py
├── README.md
├── requirements.txt

Tecnologías Utilizadas
Python 3
Pandas
Matplotlib
Git & GitHub
⚡ Instalación
Clonar repositorio:
git clone <https://github.com/KarenSC-0591/proyecto_final_grupo2_bigdata.git>
Crear entorno virtual:
python -m venv venv
Activar entorno:
venv\Scripts\activate
Instalar dependencias:
pip install -r requirements.txt
▶️ Ejecución
📊 Visualización de ventas
py sales_monitoring/src/visualization.py
🚨 Validación de datos
py data_quality_checker/src/validation.py
📝 Generar reporte
py data_quality_checker/src/report.py
📌 Conclusión

El proyecto permite analizar y validar datasets de forma automatizada, facilitando la toma de decisiones basada en datos confiables.