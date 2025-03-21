from operadores.operators import Operadores

try:
    number1 = float(input("Insira o primeiro número: "))
    number2 = float(input("Insira o segundo número: "))

    operation = Operadores(number1, number2)

    results = {
        "somar": operation.soma(),
        "subtrair": operation.subtrair(),
        "multiplicar": operation.multiplicar(),
        "dividir": operation.dividir()
    }

    print("------Insira abaixo alguma opção------")
    action = str(input("| + | - | x | % | all |: ")).strip().lower()

    if action == "+":
        print(results.get("somar"))
    elif action == "-":
        print(results.get("subtrair"))
    elif action == "x":
        print(results.get("multiplicar"))
    elif action == "%":
        print(results.get("dividir"))
    elif action == "all":
        print(f"""
            Soma: {results.get("somar")}
            Subtração: {results.get("subtrair")}
            Multiplicação: {results.get("multiplicar")}
            Dividir: {results.get("dividir")}
        """)
    else:
        print("Opção inválida")
except ValueError as err:
    print(f"Error: {err}")