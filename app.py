from flask import Flask, render_template, request

app = Flask(__name__)


# Calculator logic
def add(number1, number2):
    return number1 + number2


def sub(number1, number2):
    return number1 - number2


def mul(number1, number2):
    return number1 * number2


def div(number1, number2):
    return number1 / number2


@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == 'add':
            result = add(num1, num2)
        elif operation == 'sub':
            result = sub(num1, num2)
        elif operation == 'mul':
            result = mul(num1, num2)
        elif operation == 'div':
            result = div(num1, num2)

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
