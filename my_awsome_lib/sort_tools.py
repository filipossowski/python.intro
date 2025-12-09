def bubble_sort(tab):
    n = len(tab)
    for i in range(n):
        for j in range(0, n-i-1):
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]
    return tab

def insertion_sort(tab):
    for i in range(1, len(tab)):
        klucz = tab[i]
        j = i - 1

        while j >= 0 and tab[j] > klucz:
            tab[j+1] = tab[j]
            j -= 1
        tab[j + 1] = klucz
    return tab

def selection_sort(tab):

    for i in range(len(tab)-1):
        min_index = i
        for j in range(i+1, len(tab)):
            if tab[min_index] > tab[j]:
                min_index = j
        tab[i], tab[min_index] = tab[min_index], tab[i]
        
    return tab

def merge_sort(tab):
    n = len(tab)
    size = 1
    while size < n:
        for i in range(n-1, (i+1)*size):
            left_start = i
            left_end = min(i + (size-1), n-1)
            right_start = left_end + 1
            right_end = min((i+2)*(size-1), n-1)
            if right_start < n:
                

def is_sorted(tab):
    for i in range(len(tab)-1):
        if tab[i] > tab[i+1]:
            return False
    return True
           

x = [1,3,10,0,2,5,0,3,9,1]
print(selection_sort(x))
print(is_sorted(x))