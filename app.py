from flask import Flask, render_template, request
from fractions import Fraction
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']

            if operation == 'add':
                result = num1 + num2
            elif operation == 'sub':
                result = num1 - num2
            elif operation == 'mul':
                result = num1 * num2
            elif operation == 'div':
                result = num1 / num2 if num2 != 0 else 'Undefined (division by zero)'
            elif operation == 'square':
                result = num1 ** 2
            elif operation == 'squareroot':
                result = math.sqrt(num1)
            elif operation == 'cube':
                result = num1 ** 3
            elif operation == 'cuberoot':
                result = num1 ** (1/3)
            elif operation == 'rational':
                result = str(Fraction(num1).limit_denominator())  # example: 0.75 -> '3/4'
            elif operation == 'decimal':
                result = f"{num1:.4f}"  # adjust number of decimals here

        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
