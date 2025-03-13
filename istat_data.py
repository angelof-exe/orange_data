import pandas as pd

# Fonte dei Dati "https://www.istat.it/it/files/2020/05/19_Sicilia_Scheda.pdf"

def load_istat_data():
    data = {
        'Provincia': ['Trapani', 'Palermo', 'Messina', 'Agrigento', 'Caltanissetta', 'Enna', 'Catania', 'Ragusa', 'Siracusa'],
        'Imprese Commercio': [86257, 70000, 65000, 28000, 18000, 10000, 90000, 20000, 25000],
        'Imprese Agricoltura': [30000, 25000, 22000, 19000, 12000, 8000, 27000, 15000, 17000],
        'Popolazione 0-14': [12.3, 13.2, 12.8, 11.7, 12.0, 11.1, 13.5, 11.9, 12.4],
        'Popolazione 65+': [18.4, 21.2, 20.3, 22.5, 21.7, 23.1, 19.8, 20.5, 21.1],
        'Attrazione (%)': [20.2, 24.1, 25.0, 19.4, 19.5, 23.4, 32.2, 18.1, 21.7],
        'Autocontenimento (%)': [60.4, 68.0, 60.7, 60.3, 65.1, 59.9, 50.6, 68.8, 59.1],
        'Povertà Relativa (%)': [26.0, 22.5, 24.3, 27.1, 23.7, 28.4, 21.9, 22.6, 23.2]
    }
    df = pd.DataFrame(data)
    return df
