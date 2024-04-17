import pytest

from ejemploExcepciones import EjemploExcepciones

def testZeroDivisionError():
    ejemplo = EjemploExcepciones()
    with pytest.raises(ZeroDivisionError):
        ejemplo.zeroDivisionError(num = 2, den = 0)

    
    assert ejemplo.zeroDivisionError(num = 4, den = 2) == 2