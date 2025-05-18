#!/bin/python

from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)


@app.route("/")
def index():
    # Wczytaj dane
    df = pd.read_csv("data.csv", parse_dates=["DATA"])

    # Tworzenie wykresu
    plt.figure(figsize=(10, 5))
    plt.plot(df["DATA"], df["WARTOSC"], marker="o")
    plt.title("Wykres Liniowy")
    plt.xlabel("Data")
    plt.ylabel("Wartość")
    plt.grid(True)

    # Zapisz wykres do pamięci jako obraz PNG
    img = BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode("utf8")
    plt.close()

    # Konwersja danych do HTML (tabela)
    tabela_html = df.reset_index().to_html(index=False, classes="tabela", border=1)

    return render_template("index.html", plot_url=plot_url, tabela=tabela_html)


if __name__ == "__main__":
    app.run(debug=True)
