from operadores.operators import Operadores

def operators(number1, number2):
    """
    >>> operators(2, 3).somar()
    5
    >>> operators(2, 3).subtrair()
    -1
    >>> operators(2, 3).multiplicar()
    6
    >>> operators(2, 3).dividir()
    0.6666666666666666
    """

    return Operadores(number1, number2)


if __name__ == "__main__":
    from doctest import testmod

    testmod()