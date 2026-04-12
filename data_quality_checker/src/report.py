import pandas as pd
import os

def generate_report():
    # 1. Definir rutas y asegurar que la carpeta de salida exista
    output_dir = "data_quality_checker/outputs"
    data_path = "data_quality_checker/data/proyecto3_empleados.csv"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 2. Cargar los datos (Necesario para que 'df' exista en este script)
    try:
        df = pd.read_csv(data_path)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo de datos en {data_path}")
        return

    # 3. Generar el reporte y escribir en el archivo
    with open(f"{output_dir}/errors.txt", "w") as f:
        f.write("REPORTE DE CALIDAD DE DATOS\n")
        f.write("="*30 + "\n\n")

        f.write("Valores nulos por columna:\n")
        f.write(str(df.isnull().sum()) + "\n\n")

        f.write("Tipos de datos:\n")
        f.write(str(df.dtypes) + "\n\n")

        f.write(f"Total de registros duplicados: {df.duplicated().sum()}\n")
    
    print(f"Reporte generado exitosamente en: {output_dir}/errors.txt")

if __name__ == "__main__":
    generate_report()