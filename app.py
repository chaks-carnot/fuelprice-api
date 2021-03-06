from flask import Flask, jsonify
from flask.helpers import make_response

import urls
import scrapy

app = Flask(__name__)

@app.route('/fuelprice/v1.0/diesel/', methods=['GET'])
def diesel_prices_all():
    all_diesel_prices = scrapy.scrape_all_diesel_prices()
    return make_response(jsonify(all_diesel_prices))

@app.route('/fuelprice/v1.0/diesel/<string:city_name>', methods=['GET'])
def diesel_price(city_name):
    url = urls.diesel_url(city_name.lower())
    price = scrapy.scrape_latest_price(url)
    return make_response(jsonify({city_name.title() : price}))

@app.route('/fuelprice/v1.0/petrol/', methods=['GET'])
def petrol_prices_all():
    all_petrol_prices = scrapy.scrape_all_petrol_prices()
    return make_response(jsonify(all_petrol_prices))

@app.route('/fuelprice/v1.0/petrol/<string:city_name>', methods=['GET'])
def petrol_price(city_name):
    url = urls.petrol_url(city_name.lower())
    price = scrapy.scrape_latest_price(url)
    return make_response(jsonify({city_name.title() : price}))

@app.route('/fuelprice/v1.0/city', methods=['GET'])
def all_cities():
    return make_response(jsonify({'city' : urls.city_urls_petrol.keys()}))

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}))

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
