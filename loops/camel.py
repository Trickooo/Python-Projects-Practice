toConvert = input("camelCase: ")

for i in toConvert:
    if i.isupper():
        toConvert = toConvert.replace(i, f"_{i}")
        
toConvert = toConvert.lower()
if toConvert.islower() and "_" not in toConvert:
    print("snake_case:", toConvert)
else:
    print("snake_case:", toConvert)