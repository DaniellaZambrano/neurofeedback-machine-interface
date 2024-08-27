from NeuroPy import NeuroPy
from time import sleep

import csv
import matplotlib.pyplot as plt
from datetime import datetime

neuropy = NeuroPy.NeuroPy()

timestamps = []
attention_values = []
meditation_values = []
theta_values = []
alpha_values = []
delta_values = []

def signal_callback(value):
    current_time = datetime.now().strftime("%H:%M:%S.%f") 
    attention = neuropy.attention
    meditation = neuropy.meditation
    # Cambiar si hay una propiedad específica que no sea rawValue
    theta = neuropy.rawValue  
    alpha = neuropy.rawValue  
    delta = neuropy.rawValue  

    # Se guardan los valores
    timestamps.append(current_time)
    attention_values.append(attention)
    meditation_values.append(meditation)
    theta_values.append(theta)
    alpha_values.append(alpha)
    delta_values.append(delta)

    print(f"Time: {current_time}, Attention: {attention}, Meditation: {meditation}, Theta: {theta}, Alpha: {alpha}, Delta: {delta}")


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
with open("neurodata.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Attention", "Meditation", "Theta", "Alpha", "Delta"])
    for i in range(len(timestamps)):
        writer.writerow([timestamps[i], attention_values[i], meditation_values[i], theta_values[i], alpha_values[i], delta_values[i]])

print("Datos guardados en 'neurodata.csv'.")

# Graficar los datos
plt.figure(figsize=(10, 8))

# Graficar atención
plt.subplot(3, 1, 1)
plt.plot(timestamps, attention_values, label="Attention", color='blue')
plt.ylabel("Attention")
plt.legend()
plt.xticks(rotation=45)

# Graficar meditación
plt.subplot(3, 1, 2)
plt.plot(timestamps, meditation_values, label="Meditation", color='green')
plt.ylabel("Meditation")
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