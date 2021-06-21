#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random


# Un dataframe random pa´jugar. Considerando que x entre [0, 1], y entre [0,114] y num_goles entre [0,100]
df = pd.DataFrame(
    [random.uniform(0, 1), np.random.randint(0, 115), np.random.randint(0, 100)] for i in range(10)
)


def funcion_juego(df):
    nombres = ["Angola", "México", "Belgica", "Brasil"]

    df.columns = ["tsr", "puntos", "num_goles"]
    df["paises"] = np.resize(nombres, len(df))
    print(df)

    df["paises"] = pd.Categorical(df["paises"])
    # color = np.where(x < 1, 'k', np.where(y < 5, 'b', 'r'))
    plt.figure(figsize=(10, 10))
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
