from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
import json
import jsonify
import csv

app = Flask(__name__)
api = Api(app)


class StockChart(Resource):
    def get(self):
        csv_file_path = 'TTM.csv'
        data = {}
        with open(csv_file_path) as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                date = rows['Date']
                data[date] = rows['Close']
            return json.dumps(data, sort_keys=True)


@app.route('/stockChart')
def data():
    # here we want to get the value of user (i.e. ?user=some-value)
    stock = request.args.get('stock')
    csv_file_path = stock + ".csv"
    data = {}
    with open(csv_file_path) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for rows in csvReader:
            date = rows['Date']
            data[date] = rows['Close']
        return json.dumps(data)


@app.route('/predict')
def predict_date():
    stock = request.args.get('stock')
    date = request.args.get('date')
    csv_file_path = stock + ".csv"
    data = {}
    with open(csv_file_path) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for rows in csvReader:
            if rows['Date'] == date:
                value = rows['Close']
        data[date] = value
        return json.dumps(data)


# api.add_resource(StockChart, '/stockChart')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5002')
