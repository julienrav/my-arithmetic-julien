"""Module de calculs arithmétiques."""
def pgcd(a: int, b: int) -> int:
    """Calcule le plus grand commun diviseur (PGCD) de deux entiers.
    Utilise l'algorithme d'Euclide pour calculer le PGCD de deux entiers
    relatifs.
    Parameters
    ----------
    a : int
        Premier entier.
    b : int
        Second entier.
    Returns
    -------
    int
        Le plus grand commun diviseur positif (ou nul) de ``a`` et ``b``.
    Examples
    --------
    >>> pgcd(48, 18)
    6
    >>> pgcd(17, 13)
    1
    """
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a
