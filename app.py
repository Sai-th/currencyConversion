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
    error = None
    
    if request.method == 'POST':
        try:
            currency_from = request.form['currency_from']
            currency_to = request.form['currency_to']
            amount = float(request.form['amount'])

            # Use a reliable public API
            url = f'https://api.exchangerate-api.com/v4/latest/{currency_from}'
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise an exception for bad status codes
            data = response.json()

            if currency_to in data['rates']:
                rate = data['rates'][currency_to]
                result = round(amount * rate, 2)
            else:
                error = "Currency conversion not available"
                
        except ValueError:
            error = "Please enter a valid amount"
        except requests.RequestException:
            error = "Unable to fetch exchange rates. Please try again later."
        except KeyError:
            error = "Invalid currency conversion"
        except Exception as e:
            error = f"An error occurred: {str(e)}"

    return render_template('index.html', currencies=CURRENCIES, result=result, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
