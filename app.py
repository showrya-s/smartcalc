from flask import Flask, render_template, request

# Create Flask app instance
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
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
            result = num1 / num2 if num2 != 0 else 'Cannot divide by zero'

    return render_template('index.html', result=result)

# Run locally (optional — Render uses gunicorn)
if __name__ == '__main__':
    app.run(debug=True)

