import re
import pandas as pd
import matplotlib.pyplot as plt

archivos = {
    "Argentina": "rtt_argentina.txt",
    "Chile": "rtt_chile.txt",
    "UK": "rtt_uk.txt"
}

datos = {}

for nombre, archivo in archivos.items():
    try:
        with open(archivo, "r", encoding="utf-8", errors="ignore") as f:
            contenido = f.readlines()

        rtts = []
        for linea in contenido:
            match = re.search(r"tiempo=(\d+)\s*ms", linea)
            if match:
                rtts.append(float(match.group(1)))

        datos[nombre] = pd.DataFrame({"RTT": rtts})
    
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo: {archivo}")

plt.figure(figsize=(10, 6))
for nombre, df in datos.items():
    plt.plot(df.index + 1, df["RTT"], marker='o', label=nombre)

plt.title("RTT de cada mirror")
plt.xlabel("Número de muestra")
plt.ylabel("RTT (ms)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("grafico_rtt_comparativo.png")



