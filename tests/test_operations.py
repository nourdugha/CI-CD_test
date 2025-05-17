from src.math_operations import add,sub

def test_add():
    assert add(2,3) == 5
    assert add(3,3) == 6
    assert add(-2,3) == 1
    assert add(1,2) == 3

def test_sub():
    assert sub(-1,1) == 0
    assert sub(1,1) == 0
    assert sub(4,2) == 2
    assert sub(5,3) == 2


