def change():
    expense = 23.75
    money = 100
    
    vuelto = money - expense
    pesos = int(vuelto)
    centavos = int(round((vuelto - pesos) * 100))
    
    print("\nVuelto\n")
    print("Pesos:")
    print(f"{pesos}")
    print("Centavos:")
    print(f"{centavos}")

if __name__ == "__main__":
    change()
