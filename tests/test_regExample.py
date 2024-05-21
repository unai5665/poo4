import pytest
from tests.regExample import RegExample

def test_vocales():
    assert RegExample.buscar("Erase una vez") == ["una"]

def test_url():
    assert RegExample.validURL("htp:/invalid-url") == False
    assert RegExample.validURL("https://www.example.com") == True
    assert RegExample.validURL("ftp://ftp.example.com") == True
