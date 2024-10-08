from NeuroPy import NeuroPy
from time import sleep

import csv
import matplotlib.pyplot as plt
from datetime import datetime

neuropy = NeuroPy.NeuroPy()

timestamps = []
attention_values = []
theta_values = []
alpha_values = []
beta_values = []

def signal_callback(value):
    current_time = datetime.now().strftime("%H:%M:%S.%f") 
    attention = neuropy.attention

    # Cambiar si hay una propiedad específica que no sea rawValue
    theta = neuropy.rawValue  
    alpha = neuropy.lowAlpha 
    beta = neuropy.lowBeta

    # Se guardan los valores
    timestamps.append(current_time)
    attention_values.append(attention)
    theta_values.append(theta)
    alpha_values.append(alpha)
    beta_values.append(beta)

    print(f"Time: {current_time}, Attention: {attention}, Theta: {theta}, Alpha: {alpha}, Beta: {beta}")


# Se puede usar cualquier otra señal
neuropy.setCallBack("attention", signal_callback)
neuropy.start()

try:
    while True:
        sleep(0.2)
except KeyboardInterrupt:
    pass
finally:
    neuropy.stop()

# Guardar los datos en un archivo CSV
with open("../Tests/neurodata.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Attention", "Theta", "Alpha", "Beta"])
    for i in range(len(timestamps)):
        writer.writerow([timestamps[i], attention_values[i], theta_values[i], alpha_values[i], beta_values[i]])

print("Datos guardados en 'neurodata.csv'.")

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

# Plotear
plt.tight_layout()
plt.show()