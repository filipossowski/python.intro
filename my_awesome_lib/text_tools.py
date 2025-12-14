def is_palindrome(text: str):
    """
    Sprawdza czy tekst jest palindromem (ignoruje spacje i wielkość liter).
    
    Args:
        text (str): Tekst do sprawdzenia.
    
    Returns:
        bool: True jeśli palindrom, False w przeciwnym razie.
    
    Raises:
        ValueError: Jeśli tekst jest pusty.
    
    Examples:
        >>> is_palindrome("Kajak")
        True
        >>> is_palindrome("python")
        False
    """
    if not text:
        raise ValueError("Tekst nie może być pusty")
    t = text.lower().replace(' ', '')
    if t == t[::-1]:
        return True
    
def delete_extra_spaces(text: str):
    """
    Usuwa nadmiarowe spacje z tekstu.
    
    Args:
        text (str): Tekst z ewentualnymi nadmiarowymi spacjami.
    
    Returns:
        str: Tekst z pojedynczymi spacjami.
    
    Raises:
        ValueError: Jeśli tekst jest pusty.
    
    Examples:
        >>> delete_extra_spaces("ala   ma   kota")
        'ala ma kota'
    """
    if not text:
        raise ValueError("Tekst nie może być pusty")
    return ' '.join(text.split())

def remove_polish_letters(text: str):
    """
    Zamienia polskie litery na łacińskie odpowiedniki.
    
    Args:
        text (str): Tekst z polskimi literami.
    
    Returns:
        str: Tekst bez polskich liter (małe litery).
    
    Raises:
        ValueError: Jeśli tekst jest pusty.
    
    Examples:
        >>> remove_polish_letters("ąęćłńóśźż")
        'acelnoszzz'
    """
    if not text:
        raise ValueError("Tekst nie może być pusty")
    x = text.lower()
    polish_to_latin = {
        'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n',
        'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'
    }
    for polish, latin in polish_to_latin.items():
        x = x.replace(polish, latin)
    return x

def trim(text: str):
    """
    Usuwa białe znaki z początku i końca tekstu.
    
    Args:
        text (str): Tekst do przycięcia.
    
    Returns:
        str: Tekst bez białych znaków na końcach.
    
    Raises:
        ValueError: Jeśli tekst jest pusty.
    
    Examples:
        >>> trim("  ala ma kota  ")
        'ala ma kota'
    """
    if not text:
        raise ValueError("Tekst nie może być pusty")
    return text.strip()

def word_count(text: str):
    """
    Liczy słowa w tekście.
    
    Args:
        text (str): Tekst do analizy.
    
    Returns:
        int: Liczba słów.
    
    Raises:
        ValueError: Jeśli tekst jest pusty.
    
    Examples:
        >>> word_count("ala ma kota")
        3
    """
    if not text:
        raise ValueError("Tekst nie może być pusty")
    words = text.split()
    return len(words)

def contains(text: str, substring: str):
    """
    Sprawdza czy tekst zawiera podciąg.
    
    Args:
        text (str): Tekst do przeszukania.
        substring (str): Szukany podciąg.
    
    Returns:
        bool: True jeśli zawiera, False w przeciwnym razie.
    
    Raises:
        ValueError: Jeśli któryś argument jest pusty.
    
    Examples:
        >>> contains("ala ma kota", "ma")
        True
    """
    if not text or not substring:
        raise ValueError("Tekst i podciąg nie mogą być puste")
    if substring in text:
        return True