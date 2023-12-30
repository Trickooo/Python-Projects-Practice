def main():
    fuel = input("Fraction: ")
    x, y = fuel.split("/")
    divide(x, y)


def divide(x, y):
    try:
        z = (int(x) / int(y))*100
        if z == 100:
            print("F")
        elif z <= 1 and z >= 0:
            print("E")
        elif z > 100 or z < 0:
            raise ValueError
        else:
            print(f"{int(z)}%")
    except(ValueError, ZeroDivisionError):
        main()

main()