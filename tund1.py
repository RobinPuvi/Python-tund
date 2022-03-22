#calculator
#plus
def plus (a, b):
    return a+b
#minus
def minus (a, b):
    return a-b
#multiply *
def multiply (a,b):
    return a*b
#divide /
def divide (a,b):
    return a/b
while 1:
    print("Kas sa tahad liita, lahutada, korrutada või jagada? (sisesta +,-,* või /)")
    question = input("-> ") #question if +,-,* or /
    if question == "+": #input +
        muutuja1 = int(input("Sisesta number 1 -> "));
        muutuja2 = int(input("Sisesta number 2 -> "))
        tulemus = plus(muutuja1, muutuja2)
        print (tulemus)
    if question == "-": #input -
        muutuja1 = int(input("Sisesta number 1 -> "));
        muutuja2 = int(input("Sisesta number 2 -> "))
        tulemus = minus(muutuja1, muutuja2)
        print (tulemus)
    if question == "*": #input +
        muutuja1 = int(input("Sisesta number 1 -> "));
        muutuja2 = int(input("Sisesta number 2 -> "))
        tulemus = multiply(muutuja1, muutuja2)
        print (tulemus)
    if question == "/": #input -
        muutuja1 = int(input("Sisesta number 1 -> "));
        muutuja2 = int(input("Sisesta number 2 -> "))
        tulemus = divide(muutuja1, muutuja2)
        print (tulemus)
    else:
        print ("Vale sisend")