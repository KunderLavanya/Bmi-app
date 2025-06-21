from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bmi_calculator():
    bmi = None
    category = ''
    category_class = ''
    error = None
    name = ""

    if request.method == 'POST':
        try:
            name = request.form['name']
            weight = float(request.form['weight'])
            height = float(request.form['height'])

            if weight <= 0 or height <= 0:
                raise ValueError("Weight and height must be positive numbers.")

            bmi = round(weight / (height ** 2), 2)

            if bmi < 18.5:
                category = "Underweight"
                category_class = "underweight"
            elif 18.5 <= bmi < 24.9:
                category = "Normal weight"
                category_class = "normal"
            elif 25 <= bmi < 29.9:
                category = "Overweight"
                category_class = "overweight"
            else:
                category = "Obese"
                category_class = "obese"

        except ValueError as ve:
            error = str(ve)
        except:
            error = "Invalid input. Please enter valid numbers."

    return render_template('index.html', bmi=bmi, category=category, category_class=category_class, error=error, name=name)

if __name__ == '__main__':
    app.run(debug=True)