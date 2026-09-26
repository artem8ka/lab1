from toolkit.calculator import calculator_function


def test_1():
    assert calculator_function('')

def test_2():
    assert calculator_function('2+2+abc')

def test_3():
    assert calculator_function('*4-3')

def test_4():
    assert(calculator_function('-2*52/'))

def test_5():
    assert calculator_function('5--432**3')

def test_6():
    assert calculator_function('2+4*49--++-+-2/0*1234')

def test_7():
    assert calculator_function('2+2*2')

def test_8():
    assert calculator_function('0*52145+124-6*8/2-50')

def test_9():
    assert calculator_function('0.5*50')

def test_10():
    assert calculator_function('256/4')

def test_11():
    assert calculator_function('00005+4')

def test_12():
    assert calculator_function('0.32/2')