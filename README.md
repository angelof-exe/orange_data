# 🍊 OrangeData - Dashboard di Monitoraggio Settore Primario

Questa dashboard interattiva utilizza Dash e Plotly per visualizzare dati ambientali e statistici sul settore primario.

## Requisiti
- Python 3.x
- Pip
- Ambiente virtuale Python (consigliato)

## Installazione e Avvio

### 1. Creazione e Attivazione dell'Ambiente Virtuale
Si consiglia di utilizzare un ambiente virtuale per isolare le dipendenze del progetto.

**Su Windows:**
```sh
python -m venv venv
venv\Scripts\activate
```

**Su macOS/Linux:**
```sh
python3 -m venv venv
source venv/bin/activate
```

### 2. Installazione delle Dipendenze
Una volta attivato l'ambiente virtuale, installa i pacchetti richiesti:
```sh
pip install -r requirements.txt
```

### 3. Avvio della Dashboard
Per avviare la dashboard eseguire:
```sh
python main.py
```
La dashboard sarà accessibile all'indirizzo `http://127.0.0.1:8050/` nel browser.

## Struttura del Progetto
- `main.py`: Contiene la logica principale della dashboard.
- `generate_data.py`: Genera dati ambientali simulati.
- `istat_data.py`: Carica i dati statistici da fonti ufficiali.
- `requirements.txt`: Elenco delle dipendenze necessarie.

## Note
Se si verificano problemi con le dipendenze, assicurarsi di avere una versione aggiornata di `pip`:
```sh
pip install --upgrade pip
```

