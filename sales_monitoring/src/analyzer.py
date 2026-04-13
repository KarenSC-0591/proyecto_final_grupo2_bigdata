import pandas as pd

def analyze_sales():
    df = pd.read_csv("sales_monitoring/data/proyecto2_ventas.csv")

    # Crear total
    df["total"] = df["Sales"] * df["Quantity"]

    print("Total de ventas:", df["total"].sum())

    print("\nVentas por producto:")
    print(df.groupby("Product Name")["total"].sum())

    print("\nPromedio de ventas:")
    print(df["total"].mean())

if __name__ == "__main__":
    analyze_sales()