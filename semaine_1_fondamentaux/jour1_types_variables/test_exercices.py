from exercices import somme, detecte_type

def test_somme():
    assert somme(3, 4) == 7
    assert somme(-1, 1) == 0

def test_detecte_type():
    assert detecte_type(42) == int
    assert detecte_type(3.14) == float
    assert detecte_type("hello") == str
