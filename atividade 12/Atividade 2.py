from flask import Flask, render_template, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

# Log de acesso
@app.before_request
def log_request():
    print(f"Acesso: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Função para obter o preço do Bitcoin em uma moeda específica
def get_bitcoin_price(currency):
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        price = data["bpi"].get(currency, {}).get("rate", "N/A")
        return price, data["time"]["updated"]
    return None, None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bitcoin/usd')
def bitcoin_usd():
    price, updated_time = get_bitcoin_price("USD")
    return render_template('bitcoin.html', currency="USD", price=price, updated_time=updated_time)

@app.route('/bitcoin/eur')
def bitcoin_eur():
    price, updated_time = get_bitcoin_price("EUR")
    return render_template('bitcoin.html', currency="EUR", price=price, updated_time=updated_time)

@app.route('/bitcoin/gbp')
def bitcoin_gbp():
    price, updated_time = get_bitcoin_price("GBP")
    return render_template('bitcoin.html', currency="GBP", price=price, updated_time=updated_time)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
