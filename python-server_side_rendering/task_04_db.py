from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)
source_author = ["json", "csv", "sql"]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open('items.json') as f:
        items = json.load(f)
    return render_template('items.html', items=items.get("items"))


@app.route('/products')
def products():
    error = 0
    source = request.args.get('source')
    id = request.args.get('id')

    if (source not in source_author):
        value = "Wrong source"
        error = 1
    else:
        if (source == "json"):
            value = read_json()
        elif (source == "csv"):
            value = read_csv()
        else:
            value = read_sql()
        if id:
            success = 0
            for element in value:
                if (id == str(element['id'])):
                    success = 1
                    value = [element]
            if success == 0:
                value = "Product not found"
                error = 1
    return render_template('product_display.html', value=value, error=error)


def read_csv():
    with open('products.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        result = list(reader)
    return result


def read_json():
    with open('products.json') as f:
        value = json.load(f)
    return value


def read_sql():
    conn = sqlite3.connect("products.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('select * from Products')
    rows = cur.fetchall()
    conn.close()
    return rows


if __name__ == '__main__':
    app.run(debug=True, port=5000)
