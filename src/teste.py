def calculador():

    while True:

        valor1 = input("Informe valor1: ").strip()

        valor2 = input("Informe valor2: ").strip()

        if len(valor1) == 0:
            valor1 = input("Informe um valor válido para valor1: ").strip()

        if len(valor2) == 0:
            valor2 = input("Informe um valor válido para valor2: ").strip()

        valor1 = int(valor1)
        valor2 = int(valor2)

        print("Você informou valor1 =", valor1)
        print("Você informou valor2 =", valor2)


calculador()
