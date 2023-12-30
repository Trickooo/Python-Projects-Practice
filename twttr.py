text = input("Input: ")
consonants = ['a', 'e', 'i', 'o', 'u']
for c in text:
    if c.lower() in consonants:
        text = text.replace(c, "")
       

print("Output:", text)
