def pgcd(a: int, b: int) -> int:
    """Calcule le plus grand commun diviseur (PGCD) de deux entiers."""
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a
