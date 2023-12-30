compute = input("Expression: ")
compute = compute.split(sep=" ")

if compute[1] == "+":
    print(float(compute[0]) + float(compute[2]))
elif compute[1] == "-":
    print(float(compute[0]) - float(compute[2]))
elif compute[1] == "/":
    print(float(compute[0]) / float(compute[2]))
elif compute[1] == "*":
    print(float(compute[0]) * float(compute[2]))
else:
    print("Please enter a valid expression.")