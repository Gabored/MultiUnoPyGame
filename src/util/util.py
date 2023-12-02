def lerp(a, b, t):
    """Interpola linealmente entre 'a' y 'b' usando 't' como factor de interpolación.

    Args:
        a (float): Valor inicial.
        b (float): Valor final.
        t (float): Factor de interpolación.

    Returns:
        float: El resultado de la interpolación lineal.
    """
    return a + (b - a) * t
