from flask import Flask, render_template, request

from lib import calculate_bmi


def main():
    app = Flask(__name__)

    @app.route('/')
    def frontpage():
        weight = request.args.get('weight')
        height = request.args.get('height')
        if weight and height:
            bmi = calculate_bmi(int(weight), int(height))
            level = 'danger' # TODO calculate based on bmi
            return render_template('index.html', title='BMI Calculation', bmi=bmi, weight=weight, height=height, level=level)

        return render_template('index.html', title='BMI Calculation')

    app.run(port=9876)


if __name__ == '__main__':
    main()
