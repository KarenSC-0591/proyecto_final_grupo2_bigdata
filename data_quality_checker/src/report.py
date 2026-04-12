import pandas as pd


def generate_report():
    df = pd.read_csv("data_quality_checker/data/proyecto3_empleados.csv")

    with open("data_quality_checker/outputs/errors.txt", "w") as f:
        f.write("REPORTE DE CALIDAD DE DATOS\n\n")

        f.write("Valores nulos:\n")
        f.write(str(df.isnull().sum()))

        f.write("\n\nDuplicados:\n")
        f.write(str(df.duplicated().sum()))


if __name__ == "__main__":
    generate_report()