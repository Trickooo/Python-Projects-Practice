def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    validity = False
    numbers = []
    for i in s:
        if i.isdigit():
            numbers.append(i)

    if s.isalnum():
        if len(s) >= 2 and len(s) <= 6:
            if s[0].isalpha() and s[1].isalpha():
                if numbers[0] != '0' and s[-1].isdigit():
                    validity = True

    if validity == True:
        return True
    else:    
        return False

main()