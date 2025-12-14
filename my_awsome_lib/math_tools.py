def fibonacci(n: int): 
    """
    Oblicza n-ty wyraz ciągu Fibonacciego (iteracyjnie).
    
    Args:
        n (int): Numer wyrazu ciągu (n >= 0).
    
    Returns:
        int: n-ty wyraz ciągu Fibonacciego.
    
    Raises:
        ValueError: Jeśli n jest ujemne.
    
    Examples:
        >>> fibonacci(0)
        0
        >>> fibonacci(5)
        5
        >>> fibonacci(10)
        55
    """
    if n < 0:
        raise ValueError("n musi być nieujemne")
    if n == 0:
        return 0
    if n == 1 :
        return 1
    
    a = 0
    b = 1
    for i in range(2, n):
        c = a + b 
        a = b
        b = c 

    return b

def bmi(weight: float, height: float):
    """
    Oblicza BMI i zwraca kategorię wagową.
    
    Args:
        weight (float): Masa ciała w kg.
        height (float): Wzrost w metrach.
    
    Returns:
        str: Kategoria BMI ('niedowaga', 'norma', 'nadwaga', 'otyłość').
    
    Examples:
        >>> bmi(70, 1.75)
        'norma'
        >>> bmi(90, 1.70)
        'nadwaga'
    """
    bmi_value = weight / (height ** 2)
    category = ""
    if bmi_value < 18.5:
        category = "niedowaga"
    elif bmi_value < 25:
        category = "norma"
    elif bmi_value < 30:
        category = "nadwaga"
    elif bmi_value >= 30:
        category = "otyłość"

    return category

def mean(tab: list[float]):
    """
    Oblicza średnią arytmetyczną elementów listy.
    
    Args:
        tab (list[float]): Lista liczb.
    
    Returns:
        float: Średnia arytmetyczna.
    
    Raises:
        ValueError: Jeśli lista jest pusta.
    
    Examples:
        >>> mean([1, 2, 3])
        2.0
    """
    if len(tab) == 0:
        raise ValueError("Lista nie moze być pusta.")
    return sum(tab)/len(tab)

def sum_list(numbers: list[float]):
    """
    Oblicza sumę elementów listy liczb.
    
    Args:
        numbers (list[float]): Lista liczb do zsumowania.
    
    Returns:
        float: Suma elementów listy.
    
    Raises:
        ValueError: Jeśli lista jest pusta lub zawiera nie-liczby.
    
    Examples:
        >>> sum_numbers([1, 2, 3])
        6.0
    """
    if not isinstance(numbers, list):
        raise ValueError("Argument musi być listą")
    if len(numbers) == 0:
        raise ValueError("Lista nie może być pusta")
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("Lista może zawierać tylko liczby")
    x = 0.0
    for n in numbers:
        x = x + n
    return x


def is_even(n: int):
    """
    Sprawdza czy liczba jest parzysta.
    
    Args:
        n (int): Liczba do sprawdzenia.
    
    Returns:
        bool: True jeśli parzysta, False w przeciwnym razie.
    
    Raises:
        ValueError: Jeśli n nie jest liczbą całkowitą.
    
    Examples:
        >>> is_even_number(4)
        True
    """
    if not isinstance(n, int):
        raise ValueError("n musi być liczbą całkowitą")
    return n % 2 == 0
    

def absolute(n: float):
    """
    Zwraca wartość bezwzględną liczby.
    
    Args:
        n (float): Liczba.
    
    Returns:
        float: Wartość bezwzględna |n|.
    
    Raises:
        ValueError: Jeśli n nie jest liczbą.
    
    Examples:
        >>> absolute(-5)
        5.0
    """
    if not isinstance(n, (int, float)):
        raise ValueError("n musi być liczbą")
    if n < 0:
        return -n
    return n
    


print(fibonacci(0))