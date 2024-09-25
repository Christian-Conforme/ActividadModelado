import pytest
from calculadora import sumar, restar, multiplicar, dividir

def test_sumar():
    assert sumar(3, 2) == 5
    assert sumar(-1, 1) == 0
    assert sumar(-1, -1) == -2

def test_restar():
    assert restar(3, 2) == 1
    assert restar(5, 10) == -5
    assert restar(-1, -1) == 0

def test_multiplicar():
    assert multiplicar(3, 2) == 6
    assert multiplicar(-1, 1) == -1
    assert multiplicar(-1, -1) == 1

def test_dividir():
    assert dividir(6, 3) == 2
    assert dividir(5, 0) == "Error: No se puede dividir entre cero."
    assert dividir(-6, -3) == 2
    assert dividir(-6, 2) == -3
