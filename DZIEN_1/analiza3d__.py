# -*- coding: utf-8 -*-
"""analiza3D__.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11GaJn8f-2wKvZnirHKSZ-XjCm4IbWrth

Opis -> analiza danych z 10 czujników przez 24 godziny co 10 minut
Tensor [10,144,3] -> 10 czujników, 144 pomiary, 3 parametry (temperatura,wilgotoność,ciśnienie)
"""

import numpy as np
import pandas as pd

#tworzymy tesnsor 3D (czujnik, czas, parametr)
np.random.seed(42)
num_sensors = 10
time_steps = 144
num_features = 3

tensor_data = np.random.normal(loc=[22,50,1013],scale=[1,5,10],
                               size=(num_sensors,time_steps,num_features))

print(f"kształt tensora: {tensor_data.shape}")

#przekształcenie do formatu DataFrame
sensor_ids = np.arange(1,num_sensors+1)
time_index = pd.date_range("2025-05-07",periods=time_steps,freq="10min")
feature_names = ["temperature","humidity","pressure"]

records = []
for sensor in range(num_sensors):
    for t in range(time_steps):
        record = {
            "sensor_id":sensor_ids[sensor],
            "timestamp":time_index[t],
            "temperature":tensor_data[sensor,t,0],
            "hunidity":tensor_data[sensor,t,1],
            "pressure":tensor_data[sensor,t,2]
        }
        records.append(record)

df = pd.DataFrame.from_records(records)

df.head(5)

#przykład analizy - srednia temperatura każdego czujnika
avg_temp = df.groupby("sensor_id")["temperature"].mean()
print(f"\nŚrednia temperatura na czujnik\n {avg_temp}")

import matplotlib.pyplot as plt

sensor1 = df[df["sensor_id"]==1]
plt.plot(sensor1["timestamp"],sensor1["temperature"])
plt.title("Temperatura - czujnik 1")
plt.xlabel("Czas")
plt.ylabel("Temperatura [C]")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()