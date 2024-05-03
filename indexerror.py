def seleccionar_fruta(indice):
    frutas = ["manzana", "plátano", "pera"]
    try:
        fruta_seleccionada = frutas[indice]
        return fruta_seleccionada
    except IndexError:
        print(None)
 
