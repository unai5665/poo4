import re
import rich
from rich import console, table


console = console.Console()
table = table.Table(header_style="green")
table.add_column("Funciones", style="dim", width=12)
table.add_column("Variables", style="dim", width=12)
table.add_column("Líneas", style="dim", width=12)


class AnaPython:
    @staticmethod
    def countDef(codigo: str) -> int:
        patron = "def\\s+\\w+\\(.*\\)\\s*(->\\s*\\w+)?\\s*:"
        resultado = re.findall(patron, codigo)
        return len(resultado)

    @staticmethod
    def countVar(codigo: str) -> int:
        patron = "\\b(\\w+)\\s*=\\s*[^=]"
        resultado = re.findall(patron, codigo)
        return len(resultado)

    def countLin(codigo: str) -> int:
        patron = "\\n"
        resultado = re.findall(patron, codigo)
        return len(resultado) + 1


if __name__ == '__main__':
    codigo = '''
        def suma(a, b):
            fer=3

        def multipli(a: int, b: int) -> int:

        def error espacios():

        def imprimir():

        def sinDosPuntos()

        def sin_argumentos():
            hola = "fer"

        defmalformada: '''

    cantDef = AnaPython.countDef(codigo)
    cantVar = AnaPython.countVar(codigo)
    cantLin = AnaPython.countLin(codigo)
    table.add_row(f"{cantDef}", f"{cantVar}", f"{cantLin}")
    console.print(table)