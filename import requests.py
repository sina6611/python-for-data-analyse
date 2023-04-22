import requests
import json
import matplotlib.pyplot as plt

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
response = requests.get(url)
data = response.json()

# Extrahieren Sie die Schlusskurse aus den Daten
close_prices = []
for time, values in data['Time Series (5min)'].items():
    close_prices.append(float(values['4. close']))

# Erstellen Sie ein Diagramm mit den Schlusskursen
plt.plot(close_prices)
plt.title('IBM Schlusskurse (24 Stunden)')
plt.xlabel('Zeit')
plt.ylabel('Preis')
plt.show()
