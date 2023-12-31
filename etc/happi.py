import cowsay
import pyttsx3

engine = pyttsx3.init()
this = input("What's the Occation? ")
if this.lower() == "new year":
        greet = "Happy new year bebe ko Julienne aubrey ruela, salamat sa isa pang taon na kasama kita at parati mo sanang tatandaan na mahal kita at parati akong mananatili para sayo. Isang bagong taon para satin, I love you! Mwah mwah"
        cowsay.stegosaurus(greet)
        engine.say(greet)
        engine.runAndWait()