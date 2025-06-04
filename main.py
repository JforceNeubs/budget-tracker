# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

transactions = []  # List to hold all income and expenses

@app.route('/')
def index():
    balance = sum(t['amount'] for t in transactions)
    return render_template('index.html', transactions=transactions, balance=balance)

@app.route('/add', methods=['POST'])
def add_transaction():
    name = request.form.get('name')
    amount = float(request.form.get('amount'))
    transactions.append({'name': name, 'amount': amount})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
