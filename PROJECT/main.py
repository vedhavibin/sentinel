from flask import Flask, jsonify, redirect, render_template, request
app = Flask(__name__)

# In-memory data storage (replace with a database for a production app)
budget_data = {
    'totalIncome': 0.0,
    'totalExpenses': 0.0,
    'remainingBudget': 0.0
}

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', budget_data=budget_data)

@app.route('/add_income', methods=['POST'])
def add_income():
    income_amount = float(request.form['incomeAmount'])
    budget_data.update({'totalIncome':0})
    budget_data['totalIncome'] += income_amount
    update_remaining_budget()
    return redirect('/')

@app.route('/add_expense', methods=['POST'])
def add_expense():
    expense_amount = float(request.form['expenseAmount'])
    budget_data.update({'totalExpenses':0})
    budget_data['totalExpenses'] += expense_amount
    update_remaining_budget()
    return redirect('/')

def update_remaining_budget():
    budget_data['remainingBudget'] = budget_data['totalIncome'] - budget_data['totalExpenses']

if __name__ == '__main__':
    app.run(debug=True)