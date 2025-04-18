import numpy as np
import pandas as pd

# Impostazioni del simulatore
np.random.seed(42)
num_giorni = 365
date_range = pd.date_range(start='2024-01-01', periods=num_giorni, freq='D')

# Generazione dei dati ambientali
temperature = np.random.normal(loc=20, scale=5, size=num_giorni)
umidita = np.random.uniform(low=30, high=90, size=num_giorni)
precipitazioni = np.random.exponential(scale=3, size=num_giorni)

# Generazione dei dati di produzione
quantita_raccolto = np.random.normal(loc=100, scale=20, size=num_giorni)
tempi_crescita = np.random.normal(loc=90, scale=10, size=num_giorni)

# Calcolo dell'Indice di Produttività
indice_produttivita = (quantita_raccolto / tempi_crescita) * 100

# Creazione del DataFrame
df = pd.DataFrame({
    'Data': date_range,
    'Temperatura (°C)': temperature,
    'Umidità (%)': umidita,
    'Precipitazioni (mm)': precipitazioni,
    'Quantità Raccolto (q)': quantita_raccolto,
    'Tempi Crescita (giorni)': tempi_crescita,
    'Indice Produttività': indice_produttivita
})

# Funzione per ottenere il DataFrame
def get_data():
    return df
