import re
from rich.console import Console
from rich.table import Table


class AnaPython:
    @staticmethod
    def contar_def(codigo: str) -> int:
        patron = r"def\s+\w+\(.*\)\s*(->\s*\w+)?\s*:"
        resultado = re.findall(patron, codigo)
        return len(resultado)

    @staticmethod
    def contar_var(codigo: str) -> int:
        patron = r"\b(\w+)\s*=\s*[^=]"
        resultado = re.findall(patron, codigo)
        return len(resultado)

    @staticmethod
    def contar_lin(codigo: str) -> int:
        patron = r"\n"
        resultado = re.findall(patron, codigo)
        return len(resultado) + 1


if __name__ == '__main__':
    codigo = '''
def suma(a, b):
    resultado = a + b
    return resultado

def resta(a: int, b: int) -> int:
    return a - b

def saludo(nombre):
    mensaje = f"Hola, {nombre}!"
    return mensaje

def sin_argumentos():
    hola = "mundo"
    numero = 42

variable_global = 10
'''

    cant_def = AnaPython.contar_def(codigo)
    cant_var = AnaPython.contar_var(codigo)
    cant_lin = AnaPython.contar_lin(codigo)

    table = Table(title="Estadísticas de Código Python", title_style="bold magenta", border_style="blue")
    table.add_column("Funciones", style="cyan", header_style="bold cyan")
    table.add_column("Variables", style="green", header_style="bold green")
    table.add_column("Líneas", style="yellow", header_style="bold yellow")
    table.add_row(f"{cant_def}", f"{cant_var}", f"{cant_lin}", style="dim")

    console = Console()
    console.print(table)
