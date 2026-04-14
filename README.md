📊 Data Quality & Sales Analyzer
👥 Integrantes y Roles
🧑‍💻 Karen Sánchez — Git Manager & Integración del Proyecto
🧑‍💻 Raúl — Carga de Datos (Data Ingestion)
📊 Byron — Análisis de Datos (Data Analysis)
📈 Joel — Visualización de Datos (Data Visualization)
🧑‍💻 Rommer — Validación y Reporte (Data Quality)

🧾 Descripción

Data Quality & Sales Analyzer es una solución desarrollada en Python que permite analizar y validar datos de manera automatizada.

La plataforma integra dos módulos principales:

📊 Sales Monitoring:
Permite analizar ventas, identificar productos con mayor rendimiento y calcular métricas clave.
🚨 Data Quality Checker:
Permite validar la calidad de los datos detectando valores nulos, duplicados y tipos de datos incorrectos.

El sistema facilita la toma de decisiones basada en datos confiables.

⚙️ Características
📥 Carga de datos desde archivos CSV usando pandas
📊 Análisis de ventas (totales, agrupaciones y promedios)
📈 Visualización de datos con matplotlib
🚨 Validación de calidad de datos:
Valores nulos
Duplicados
Tipos de datos
📝 Generación de reportes automáticos

🏗️ Arquitectura

El proyecto está dividido en dos módulos independientes dentro del mismo repositorio:

data_quality_checker/   → Validación de datos
sales_monitoring/       → Análisis de ventas

Cada módulo sigue una arquitectura modular basada en:

Carga de datos
Procesamiento
Salida (outputs)
📂 Estructura del Proyecto
data_quality_checker/
│
├── data/
│   └── proyecto3_empleados.csv
│
├── outputs/
│   └── errors.txt
│
├── src/
│   ├── load_data.py
│   ├── validation.py
│   ├── report.py
│   ├── main.py
│   └── rules.py


sales_monitoring/
│
├── data/
│   └── proyecto2_ventas.csv
│
├── output/
│
├── src/
│   ├── load_data.py
│   ├── analyzer.py
│   ├── visualization.py
│   └── main.py


README.md  
requirements.txt

Tecnologías Utilizadas
Python 3
Pandas
Matplotlib
Git & GitHub


Instalación
1. Clonar el repositorio
git clone https://github.com/KarenSC-0591/data_quality_sales_analyzer.git
cd data_quality_sales_analyzer

2. Crear entorno virtual
python -m venv venv

3. Activar entorno
venv\Scripts\activate

4. Instalar dependencias
pip install -r requirements.txt

Ejecución
Visualización de ventas
python sales_monitoring/src/visualization.py
Validación de datos
python data_quality_checker/src/validation.py
Generación de reporte
python data_quality_checker/src/report.py
Valor del Proyecto

Este sistema permite a empresas:

Detectar problemas en sus datos
Analizar tendencias de ventas
Tomar decisiones estratégicas basadas en información confiable

Conclusión

Data Quality & Sales Analyzer integra análisis y calidad de datos en una sola solución, facilitando procesos de negocio y mejorando la confiabilidad de la información.