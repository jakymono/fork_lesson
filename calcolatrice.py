def calculator():
    while True:
        print("Benvenuti alla Calcolatrice!")
        print("1. Addizione")
        print("2. Sottrazione")
        print("3. Moltiplicazione")
        print("4. Divisione")
        print("5. Esci")
        scelta = input("Inserisci il numero dell'operazione che desideri eseguire: ")
        try:
            scelta = int(scelta)
        except ValueError:
            print("Per favore inserire un numero valido")
            continue
        if scelta not in range(1,6):
            print("Per favore inserire una scelta valida")
            continue
        if scelta == 5:
            break
        num1 = input("Inserisci il primo numero: ")
        try:
            num1 = float(num1)
        except ValueError:
            print("Per favore inserire un numero valido")
            continue
        num2 = input("Inserisci il secondo numero: ")
        try:
            num2 = float(num2)
        except ValueError:
            print("Per favore inserire un numero valido")
            continue
        if scelta == 1:
            print("Il risultato è:", num1 + num2)
        elif scelta == 2:
            print("Il risultato è:", num1 - num2)
        elif scelta == 3:
            print("Il risultato è:", num1 * num2)
        elif scelta == 4:
            if num2 == 0:
                print("Impossibile dividere per zero")
                continue
            print("Il risultato è:", num1 / num2)
    print("Grazie per aver usato la calcolatrice!")
calculator()
def main():
    out=calculator()
    print(out)
main()
