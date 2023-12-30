def main():
    text = input("Type your Text: ")
    print(emojiCheck(text))


def emojiCheck(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")    
    return text

main()