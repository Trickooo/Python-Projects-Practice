greet = input("Greeting: ")

if "hello" in greet.strip().lower():
    print("$0")
elif greet.strip().lower().startswith("h"):
    print("$20")
else:
    print("$100")