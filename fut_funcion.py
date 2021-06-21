#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random


# Un dataframe random pa´jugar. Considerando que tsr entre [0, 1], puntos entre [0,114] y num_goles entre [0,100]
# se genera un dataframe con 10 renglones y 3 columnas que seran tsr, puntos y num_goles
df = pd.DataFrame(
    [random.uniform(0, 1), np.random.randint(0, 115), np.random.randint(0, 100)] for i in range(10)
)


def funcion_juego(df):
    """Una función para hacer gráficas de burbuja. Los países se convierten a una variable categorica
    para ser usados como códigos de color en las burbujas y el diámetro de la burbuja es representado
    por el número de goles"""

    nombres = ["Angola", "México", "Belgica", "Brasil"]
    df.columns = ["tsr", "puntos", "num_goles"]  # Nombramos columnas
    df["paises"] = np.resize(
        nombres, len(df)
    )  # Agregamos nueva columna con nombres de paises en una lista que se repite

    df["paises"] = pd.Categorical(df["paises"])
    # color = np.where(x < 1, 'k', np.where(y < 5, 'b', 'r'))
    plt.figure(figsize=(10, 10))

    # s es el diámetro de la burbuja*10 para hacer más visibles los puntos en este caso en particular
    # c es el color dependiendo del país que se seleccione. x e y son los ejes que generan los puntos en el diagrama de dispersión.
    plt.scatter(
        x=df["tsr"],
        y=df["puntos"],
        s=df["num_goles"] * 10,
        c=df["paises"].cat.codes,
        cmap="Accent",
        alpha=0.6,
        edgecolors="white",
        linewidth=2,
    )

    plt.xlabel("tsr")
    plt.ylabel("puntos")
    plt.title("Titulo de la gráfica")
    return plt.show()


funcion_juego(df)
