import cowsay
holiday = input("What Holiday it is? ")

if holiday.lower() == "christmas":
    cowsay.stegosaurus('Merry Christmas Everyone! Ho Ho Ho!')
elif holiday.lower() == "new year":
    cowsay.ghostbusters("Happy New Year!")
else:
    cowsay.cow("It's Holiday in our Hearts!")
