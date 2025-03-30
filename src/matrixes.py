def calculador():

    def validar_numero(mensagem):

        num_tentativas = 0

        vocabularios = ["NUBE", "NEFASTO", "GUERREIRO"]

        while True:

            if num_tentativas > 2:

                raise Exception("\nPois é ...acho que não foi desta vez...\n"
                                "repire fundo e tente em um outro momento.\n"
                                "\n --> Pressione qualquer tecla para encerrar <--")

            try:

                return int(input(f"{mensagem}:...").strip())

            except ValueError:

                input(
                    f"\n --> FALHA NA MATRIXES - total tentativas: {num_tentativas + 1} <--\n"
                    f"\nSério você informou um valor diferente de número, "
                    f"tente mais uma vez seu > > {vocabularios[num_tentativas]} < <!"
                )

                num_tentativas += 1

                continue

    print("\n*** Bem VINDO ao BRABBUUUUSsss ***\n")

    message = "tecle <enter> para continuar ou 'q' para sair:..."

    while input(message).strip().lower() != 'q':

        try:

            var_a = validar_numero("Informe um valor para <VARIÁVEL-A>")

            var_b = validar_numero("Informe um valor para <VARIÁVEL-B>")

            total = var_a + var_b

            print(f"\n<VARIÁVEL-A>: {var_a}"
                  f"\n<VARIÁVEL-B>: {var_b}"
                  f"\n<TOTAL PONTOS>: {total}\n")

            message = "Tecle <enter> para continuiar ou 'q' para sair..."

        except Exception as msg:

            input(msg)

            break


if __name__ == "__main__":

    calculador()
