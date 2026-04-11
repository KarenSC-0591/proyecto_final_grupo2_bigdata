import pandas as pd


def load_sales_data(file_path):
    """
    Carga el dataset de ventas.
    """

    data = pd.read_csv(file_path)

    # Estandarizar nombres de columnas
    data = data.rename(columns={
        "Order Date": "date",
        "Product Name": "product",
        "Sales": "price",
        "Quantity": "quantity"
    })

    print("Datos cargados correctamente")
    print(data.head())

    return data

if __name__ == "__main__":
    df = load_sales_data("sales_monitoring/data/proyecto2_ventas.csv")