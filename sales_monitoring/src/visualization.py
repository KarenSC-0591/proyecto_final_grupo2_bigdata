import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def plot_sales_by_product():
    df = pd.read_csv("sales_monitoring/data/proyecto2_ventas.csv")

    df["total"] = df["Sales"] * df["Quantity"]

    sales_by_product = df.groupby("Product Name")["total"].sum()

    sales_by_product.plot(kind="bar")

    plt.title("Ventas Totales por Producto")
    plt.xlabel("Producto")
    plt.ylabel("Total de Ventas")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_sales_by_product()