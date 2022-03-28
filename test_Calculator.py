import Calculator

def test_add():
    x = 20
    y = 10
    result = Calculator.add(x,y)
    assert x+y==result
def test_sub():
    x = 10
    y = 5
    result = Calculator.sub(x,y)
    assert x-y==result
def test_mul():
    x = 100
    y = 20
    result= Calculator.mul(x,y)
    assert x*y==result
def test_div():
    x = 50
    y = 5
    result = Calculator.div(x,y)
    assert x/y==result
