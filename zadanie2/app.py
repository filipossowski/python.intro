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

def fibonacci(n):
    if n < 0:
        raise ValueError
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


def is_palindrome(text):
    t = text.lower().replace(' ', '')
    if t == t[::-1]:
        return True
    else:
        return False
    

def bmi(weight, height):
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

x = bmi(59, 1.80)
print(x)