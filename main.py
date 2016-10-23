"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask, render_template, request, flash
from yahoo_finance import Share
from datetime import datetime, timedelta
from pprint import pprint

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_historical', methods=['get'])
def get_historical():
    try:
        data = {}
        stock_ticker = request.args.get('stock_ticker')
        data['stock_ticker'] = stock_ticker
        stock = Share(stock_ticker)
        start = datetime.now() - timedelta(days=30)
        end = datetime.now()
        data['info'] = stock.get_info()
        data['historical_info'] = stock.get_historical(start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d'))
        pprint(data)
    except Exception:
        flash('Invalid stock ticker %s' % request.args.get('stock_ticker'))
    return render_template('index.html', data = data)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
