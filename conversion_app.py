from flask import Flask, render_template, request
import requests

app = Flask(__name__)

CURRENCIES = {
    'USD': 'US Dollar',
    'INR': 'Indian Rupee',
    'EUR': 'Euro',
    'GBP': 'British Pound',
    'JPY': 'Japanese Yen',
    'CAD': 'Canadian Dollar',
    'AUD': 'Australian Dollar'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        currency_from = request.form['currency_from']
        currency_to = request.form['currency_to']
        amount = float(request.form['amount'])

        # Use a reliable public API
        url = f'https://api.exchangerate-api.com/v4/latest/{currency_from}'
        response = requests.get(url)
        data = response.json()

        try:
            rate = data['rates'][currency_to]
            result = round(amount * rate, 2)
        except KeyError:
            result = "Invalid currency conversion"

    return render_template('index.html', currencies=CURRENCIES, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)