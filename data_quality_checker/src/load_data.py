import pandas as pd


def load_employee_data(file_path):

    """

    Carga el dataset de empleados desde un archivo CSV.

    """

    data = pd.read_csv(file_path)

    print("Datos de empleados cargados correctamente")

    print(data.head())

    return data


if __name__ == "__main__":

    df = load_employee_data("data_quality_checker/data/proyecto3_empleados.csv")
 