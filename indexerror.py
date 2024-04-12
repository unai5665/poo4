def escoger_fruta(indice)
frutas = ["manzana", "platano", "pera"]

try:
    indice= int(input("Ingrese el índice de la fruta que desea: "))
    fruta_escogida = frutas[indice]
    print("La fruta seleccionada es:", fruta_escogida)
except IndexError:
    print("Error:No se encuentra el indice escogido")