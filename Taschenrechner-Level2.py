ErsteZahl = input("Erste Zahl: ")
Operant = input("Operant: ")
ZweiteZahl = input("Zweite Zahl: ")
if(Operant == "+"):
    ergebnis = int(ErsteZahl)+int(ZweiteZahl)
if(Operant == "-"):
    ergebnis = int(ErsteZahl)-int(ZweiteZahl)
if(Operant == "*"):
    ergebnis = int(ErsteZahl)*int(ZweiteZahl)
if(Operant == "/"):
    ergebnis = int(ErsteZahl)/int(ZweiteZahl)
print("----------------------")
print("Das Ergebnis ist: ",ergebnis)
