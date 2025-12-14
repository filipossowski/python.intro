def bubble_sort(tab: list[int]):
    """
    Sortuje listę metodą bąbelkową.
    
    Args:
        tab (list[int]): Lista do posortowania.
    
    Returns:
        list[int]: Posortowana lista rosnąco.
    
    Raises:
        ValueError: Jeśli lista jest pusta.
    
    Examples:
        >>> bubble_sort([64, 34, 25, 12, 22])
        [12, 22, 25, 34, 64]
    """
    n = len(tab)
    if n == 0:
        raise ValueError("Lista nie może być pusta.")
    for i in range(n):
        for j in range(0, n-i-1):
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]
    return tab

def insertion_sort(tab: list[int]):
    """
    Sortuje listę metodą sortowania przez wstawianie.
    
    Args:
        tab (list[int]): Lista do posortowania.
    
    Returns:
        list[int]: Posortowana lista rosnąco.
    
    Raises:
        ValueError: Jeśli lista jest pusta.
    
    Examples:
        >>> insertion_sort([12, 11, 13, 5, 6])
        [5, 6, 11, 12, 13]
    """
    if len(tab) == 0:
        raise ValueError("Lista nie może być pusta.")
    for i in range(1, len(tab)):
        klucz = tab[i]
        j = i - 1

        while j >= 0 and tab[j] > klucz:
            tab[j+1] = tab[j]
            j -= 1
        tab[j + 1] = klucz
    return tab

def selection_sort(tab: list[int]):
    """
    Sortuje listę metodą sortowania przez wybieranie.
    
    Args:
        tab (list[int]): Lista do posortowania.
    
    Returns:
        list[int]: Posortowana lista rosnąco.
    
    Raises:
        ValueError: Jeśli lista jest pusta.
    
    Examples:
        >>> selection_sort([64, 25, 12, 22, 11])
        [11, 12, 22, 25, 64]
    """
    if len(tab) == 0:
        raise ValueError("Lista nie może być pusta.")
    for i in range(len(tab)-1):
        min_index = i
        for j in range(i+1, len(tab)):
            if tab[min_index] > tab[j]:
                min_index = j
        tab[i], tab[min_index] = tab[min_index], tab[i]
        
    return tab

            
def is_sorted(tab: list[int]):
    """
    Sprawdza czy lista jest posortowana rosnąco.
    
    Args:
        tab (list[int]): Lista do sprawdzenia.
    
    Returns:
        bool: True jeśli posortowana, False w przeciwnym razie.
    
    Raises:
        ValueError: Jeśli lista jest pusta.
    
    Examples:
        >>> is_sorted([1, 2, 3, 4])
        True
        >>> is_sorted([1, 3, 2, 4])
        False
    """
    if len(tab == 0):
        raise ValueError("Lista nie może być pusta")
    for i in range(len(tab)-1):
        if tab[i] > tab[i+1]:
            return False
    return True
           
def reverse_list(tab: list[int]):
    if len(tab) == 0:
        raise ValueError("Lista nie może być pusta")
    results =[]
    for i in range(len(tab) -1, -1, -1):
        results.append(tab[i])
    return results

def swap(tab: list[int], i: int, j: int):
    """
    Wymienia elementy listy na pozycjach i i j.
    
    Args:
        tab (list[int]): Lista.
        i (int): Pierwszy indeks.
        j (int): Drugi indeks.
    
    Returns:
        None: Modyfikuje listę w miejscu.
    
    Raises:
        ValueError: Jeśli indeksy są niepoprawne.
    
    Examples:
        >>> tab = [1, 2, 3]
        >>> swap(tab, 0, 2)
        >>> tab
        [3, 2, 1]
    """
    if not (0 <= i < len(tab) and 0 <= j < len(tab)):
        raise ValueError("Indeksy muszą być w zakresie listy")
    tmp = tab[i]
    tab[i] = tab[j]
    tab[j] = tmp
