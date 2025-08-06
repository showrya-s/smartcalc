from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        operation = request.form.get('operation')
        num1 = request.form.get('num1', '').strip()
        num2 = request.form.get('num2', '').strip()

        try:
            # Only convert when needed
            if operation in ['square', 'sqrt', 'cube', 'cbrt']:
                number = float(num1)
                if operation == 'square':
                    result = number ** 2
                elif operation == 'sqrt':
                    result = math.sqrt(number)
                elif operation == 'cube':
                    result = number ** 3
                elif operation == 'cbrt':
                    result = number ** (1/3)
            else:
                number1 = float(num1)
                number2 = float(num2)
                if operation == 'add':
                    result = number1 + number2
                elif operation == 'sub':
                    result = number1 - number2
                elif operation == 'mul':
                    result = number1 * number2
                elif operation == 'div':
                    if number2 != 0:
                        result = number1 / number2
                    else:
                        result = "Error: Division by zero"
                elif operation == 'rational':
                    # Example: Return ratio
                    result = f"{number1} / {number2}"
        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template("index.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
