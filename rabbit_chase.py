import random
import math


def print_position(name, x, y, direction):
    print(f"{name} --- POSITION: ({x:>4}, {y:>4}) AND DIRECTION: {direction:>3}")


def main():
    print("RABBIT CHASE")
    print("CREATIVE COMPUTING  MORRISTOWN NEW JERSEY\n")

    T = 400
    V1 = 50
    V2 = 100
    X1 = random.randint(-500, 500)
    Y1 = random.randint(-500, 500)
    X2, Y2 = 0, 0

    print("SPEEDS (UNITS/HOP):")
    print(f"RABBIT - {V1}   YOU - {V2}\n")

    C = (X2 - X1) ** 2 + (Y2 - Y1) ** 2
    P1 = 3.141592653589 / 180
    H = 1

    while True:
        D1 = random.randint(0, 359)
        print(f"HOP#: {H:>3}")
        print(
            f" DISTANCE TO RABBIT: {math.sqrt((X2 - X1) ** 2 + (Y2 - Y1) ** 2):>4}   CLOSEST APPROACH: {math.sqrt(C):>4}\n")
        print_position("RABBIT", X1, Y1, D1)
        print_position("YOU", X2, Y2, "?")

        D2 = int(input("Enter your direction (0-359): "))

        if D2 < 0 or D2 >= 360:
            print("Invalid direction. Please enter a number between 0 and 359.")
            continue

        X3 = V1 * math.cos(D1 * P1) / 100
        Y3 = V1 * math.sin(D1 * P1) / 100
        X4 = V2 * math.cos(D2 * P1) / 100
        Y4 = V2 * math.sin(D2 * P1) / 100

        C = (X2 - X1) ** 2 + (Y2 - Y1) ** 2

        for i in range(100):
            X1 += X3
            Y1 += Y3
            X2 += X4
            Y2 += Y4

            if C < (X2 - X1) ** 2 + (Y2 - Y1) ** 2:
                break
            C = (X2 - X1) ** 2 + (Y2 - Y1) ** 2

        H += 1


if __name__ == "__main__":
    main()
