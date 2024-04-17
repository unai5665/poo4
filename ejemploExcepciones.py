class EjemploExcepciones:
    # ZeroDivisionError
    def ZeroDivisionError(self, *, num:int, den:int)->int:
        if (den == 0):
            raise ZeroDivisionError
        
        return num // den

    #ValueError
    def ValueError():
        pass

    #FileNotFoundError

    #TypeError

    #PermissionError

    #IndexError

    #KeyboardInterrupt

    #UnicodeDecodeError

    #AttributeError