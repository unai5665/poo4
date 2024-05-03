class EjemploExcepciones:
    # ZeroDivisionError
    def zeroDivisionError(self, *, num:int, den:int)->int:
        if (den == 0):
            raise ZeroDivisionError
        
        return num // den

    #ValueError
    def valueError(self):
        valor = "cadena_no_numerica"
        try:
            int(valor)
        except ValueError:
            raise ValueError("El valor no es numérico")


    #FileNotFoundError
    def fileNotFoundError(self):
        try:
            with open("archivo_que_no_existe.txt", "r"):
                pass
        except FileNotFoundError:
            raise FileNotFoundError("El archivo no se encontró")

    #TypeError
    def typeError(self):
        try:
            resultado = "10" / 2  
        except TypeError:
            raise TypeError("Operación no válida: Tipos de la operacion no compatibles")

    #PermissionError
    def permissionError(self):
        #ESTA FUNCION ES CORRECTA PERO DA ERROR YA QUE NO ESTAN CREADOS LOS ARCHIVOS QUE NECESITA
        #try:
            #with open("/Users/unaip/Desktop/privado", "w"):
                #pass
        #except PermissionError:
            raise PermissionError("Este directorio o archivo es privado :)")

    #IndexError
    def indexError(self):
        try:
            lista = [1, 2, 3]
            elemento = lista[4]  
        except IndexError:
            raise IndexError("El índice está fuera del rango de la lista")
    #KeyboardInterrupt
    def keyboardInterrupt(self):
        raise KeyboardInterrupt

    #UnicodeDecodeError
    def unicodeDecodeError(self):
         raise UnicodeDecodeError("utf-8", b'\xff', 0, 1, "mensaje de error")
    #AttributeError
    def attributeError(self):
        try:
            diccionario = {}  
            valor = diccionario.programar
        except AttributeError:
            raise AttributeError("Programar no esta en el diccionario")
