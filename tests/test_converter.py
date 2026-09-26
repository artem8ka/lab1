from toolkit.converter import converter_function


def test_1():
    assert converter_function(1000, 'kg', 'L')

def test_2():
    assert converter_function(1000, 'kg', 'm')

def test_3():
    assert converter_function(-10000, 'c', 'f')

def test_4():
    assert converter_function(-10*10, 'k', 'c')

def test_5():
    assert converter_function(-10*30, 'f', 'k')

def test_6():
    assert converter_function(534, 'mg', 'g')

def test_7():
    assert converter_function(-400, 'cm', 'm')

def test_8():
    assert converter_function(36.6, 'c', 'f')

def test_9():
    assert converter_function(52, 'c', 'k')

def test_10():
    assert converter_function(124, 'f', 'k')

def test_11():
    assert converter_function(52356, 'g', 'kg')

def test_12():
    assert converter_function(1250, 'mm', 'm')