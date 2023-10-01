from flask import Flask, render_template, request, redirect, url_for
import random
import math

app = Flask(__name__)


def print_position(name, x, y, direction):
    return f"{name} --- POSITION: ({x:>4}, {y:>4}) AND DIRECTION: {direction:>3}"


@app.route('/')
def index():
    return render_template('index.html')


T = 400
V1 = 50
V2 = 100
X1 = random.randint(-500, 500)
Y1 = random.randint(-500, 500)
X2, Y2 = 0, 0

C = (X2 - X1) ** 2 + (Y2 - Y1) ** 2
P1 = 3.141592653589 / 180
H = 0

D1 = random.randint(0, 359)
D2 = 0
distance_to_rabbit = math.sqrt((X2 - X1) ** 2 + (Y2 - Y1) ** 2)
closest_approach = math.sqrt(C)

rabbit_position = print_position("RABBIT", X1, Y1, D1)
your_position = print_position("YOU", X2, Y2, "?")


@app.route('/play', methods=['GET', 'POST'])
def play():
    global T, V1, V2, X1, Y1, X2, Y2, C, P1, H, D1, D2, distance_to_rabbit, closest_approach, rabbit_position, your_position

    if request.method == 'POST':
        H += 1
        D1 = random.randint(0, 359)
        if H != 1:
            D2 = int(request.form.get('direction'))
        X1 = V1 * math.cos(D1 * P1) / 100
        Y1 = V1 * math.sin(D1 * P1) / 100
        X2 = V2 * math.cos(D2 * P1) / 100
        Y2 = V2 * math.sin(D2 * P1) / 100

        C = (X2 - X1) ** 2 + (Y2 - Y1) ** 2

        distance_to_rabbit = math.sqrt((X2 - X1) ** 2 + (Y2 - Y1) ** 2)
        closest_approach = math.sqrt(C)

        rabbit_position = print_position("RABBIT", X1, Y1, D1)
        your_position = print_position("YOU", X2, Y2, "?")

        return render_template(
            'play.html',
            H=H,
            distance_to_rabbit=distance_to_rabbit,
            closest_approach=closest_approach,
            rabbit_position=rabbit_position,
            your_position=your_position
        )



if __name__ == '__main__':
    app.run(debug=True)
