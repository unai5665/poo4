import pytest
from indexerror import seleccionar_fruta

def test_seleccionar_fruta():
    indice_fuera_de_rango = 3
    resultado = seleccionar_fruta(indice_fuera_de_rango)
    assert resultado == None

