import Calculator
import pytest
@pytest.mark.xfail
@pytest.mark.parametrize("a,b,c",[(3,2,5),(10,2,12),(7,8,15),(2,5,8)])
def test_add(a,b,c):
    result = Calculator.add(a,b)
    assert not c ==result
@pytest.mark.parametrize("a,b,c",[(10,2,8),(10,2,18),(8,7,2),(12,5,7)])
def test_sub(a,b,c):
    result = Calculator.sub(a,b)
    assert c ==result
@pytest.mark.parametrize("a,b,c",[(3,2,5),(10,12,120),(7,8,56),(2,5,10)])
def test_mul(a,b,c):
    result= Calculator.mul(a,b)
    assert c ==result
@pytest.mark.parametrize("a,b,c",[(30,2,15),(10,2,5),(27,3,9),(12,2,6)])
def test_div(a,b,c):
    result = Calculator.div(a,b)
    assert c==result
