import matplotlib.pyplot as plt
import csv
import sys

# Verificar si se ha pasado el nombre del archivo como argumento
if len(sys.argv) < 2:
    print("Uso: python main.py <archivo.csv>")
    sys.exit(1)

# Capturar el nombre del archivo CSV del argumento
csv_file = sys.argv[1]

# Inicializar listas para los datos
timestamps = []
alpha_values = []
beta_values = []
theta_values = []

# Leer el archivo CSV
with open(csv_file, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        timestamps.append(row['Timestamp'])
        alpha_values.append(float(row['Alpha']))
        beta_values.append(float(row['Beta']))
        theta_values.append(float(row['Theta']))

# Graficar los datos
plt.figure(figsize=(10, 8))

# Graficar alpha
plt.subplot(3, 1, 1)
plt.plot(timestamps, alpha_values, label="Alpha", color='blue')
plt.ylabel("Alpha")
plt.legend()
plt.xticks(rotation=45)

# Graficar beta
plt.subplot(3, 1, 2)
plt.plot(timestamps, beta_values, label="Beta", color='green')
plt.ylabel("Beta")
plt.legend()
plt.xticks(rotation=45)

# Graficar theta
plt.subplot(3, 1, 3)
plt.plot(timestamps, theta_values, label="Theta", color='red')
plt.ylabel("Theta")
plt.legend()
plt.xticks(rotation=45)

# Ajustar diseño
plt.tight_layout()
plt.show()
