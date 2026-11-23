from my_arithmetic_julien.pgcd import pgcd


def test_pgcd_positifs():
    assert pgcd(48, 18) == 6
    assert pgcd(100, 25) == 25


def test_pgcd_premiers_entre_eux():
    assert pgcd(17, 13) == 1


def test_pgcd_avec_zero():
    assert pgcd(0, 5) == 5
    assert pgcd(5, 0) == 5
    assert pgcd(0, 0) == 0


def test_pgcd_negatifs():
    assert pgcd(-48, 18) == 6
    assert pgcd(-48, -18) == 6
