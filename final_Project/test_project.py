import pytest
from project import area_rectangulo 
from project import area_triangulo
from project import area_circulo
from project import area_paralelogramo
from project import area_trapecio
from project import area_elipse

def test_area_rectangulo():
    assert area_rectangulo(2,2)==4

def test_area_triangulo():
    assert area_triangulo(2,2)==2

def test_area_circulo():
    assert area_circulo(1)==3.1416

def test_area_paralelogramo():
    assert area_paralelogramo(10,10)==100

def test_area_trapecio():
    assert area_trapecio(10,5,4)==30

def test_area_elipse():
    assert area_elipse(10,8)==251.328