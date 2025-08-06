from flask import Flask, render_template, request
import math
from fractions import Fraction

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        try:
            num1 = request.form.get('num1')
            num2 = request.form.get('num2')
            operation = request.form['operation']

            # Convert to float or fraction depending on input
            x = float(num1) if '.' in num1 else Fraction(num1)
            y = float(num2) if num2 and '.' in num2 else Fraction(num2) if num2 else None

            # Operations
            if operation == 'add':
                result = x + y
            elif operation == 'sub':
                result = x - y
            elif operation == 'mul':
                result = x * y
            elif operation == 'div':
                result = x / y if y != 0 else 'Cannot divide by zero'
            elif operation == 'mod':
                result = x % y
            elif operation == 'floor':
                result = x // y
            elif operation == 'power':
                result = x ** y
            elif operation == 'square':
                result = x ** 2
            elif operation == 'squareroot':
                result = math.sqrt(x)
            elif operation == 'cube':
                result = x ** 3
            elif operation == 'cuberoot':
                result = x ** (1/3)
            elif operation == 'abs':
                result = abs(x)
            elif operation == 'fact':
                result = math.factorial(int(x))
            else:
                result = 'Invalid operation'
        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

