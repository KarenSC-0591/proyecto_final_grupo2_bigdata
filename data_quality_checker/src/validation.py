import pandas as pd


def validate_data():
    df = pd.read_csv("data_quality_checker/data/proyecto3_empleados.csv")

    print("Valores nulos:")
    print(df.isnull().sum())

    print("\nTipos de datos:")
    print(df.dtypes)

    print("\nDuplicados:", df.duplicated().sum())


if __name__ == "__main__":
    validate_data()