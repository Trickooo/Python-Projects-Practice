def main():
    time = input("What time is it? ")
    sum = convert(time)

    if sum >= 7.00 and sum <=8.00:
        print("Breakfast time")
    elif sum >= 12.00 and sum <= 13.00:
        print("Lunch time")
    elif sum >= 18.00 and sum <= 19.00:
        print("Dinner time")

def convert(time):
    if time.lower().endswith("a.m."):
        time = time.strip(" a.m.")
        hour, minutes = time.split(":")
    elif time.lower().endswith("p.m."):
        time = time.strip(" p.m.")
        hour, minutes = time.split(":")
        hour = float(hour) + 12.00
    else:
        hour, minutes = time.split(":")

    toMin = float(minutes) / 60
    sum = float(hour) + toMin
    return float(sum)


if __name__ == "__main__":
    main()