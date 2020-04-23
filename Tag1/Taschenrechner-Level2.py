# Eingabe der ersten Zahl, wird aus einer Zeichenkette umgewandelt in eine Zahl
ErsteZahl = int(input("Erste Zahl: "))

# Eingabe der Operation
Operation = input("Operation: ")

# Eingabe der zweiten Zahl, wir ebenfalls zu einer Zahl umgewandelt
ZweiteZahl = int(input("Zweite Zahl: "))

# Verzweigungen für die Rechenoperation

# wenn die Operation + ist:
if(Operation == "+"):
    ergebnis = ErsteZahl + ZweiteZahl

# oder wenn die Operation - ist:
elif(Operation == "-"):
    ergebnis = ErsteZahl - ZweiteZahl

# oder wenn die Operation * ist:
elif(Operation == "*"):
    ergebnis = ErsteZahl * ZweiteZahl

# oder wenn die Operation / ist:
elif(Operation == "/"):
    ergebnis = ErsteZahl / ZweiteZahl

else:
    print("Die Operation ist leider ungültig! Versuche es noch einmal.")
    exit()
print("Das Ergebnis ist: ",ergebnis)
