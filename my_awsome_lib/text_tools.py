def is_palindrome(text):
    t = text.lower().replace(' ', '')
    if t == t[::-1]:
        return True
    else:
        return False
    
def delete_extra_spaces(text):
    return ' '.join(text.split())

def remove_polish_letters(text):
    x = text.lower()
    polish_to_latin = {
        'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n',
        'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'
    }
    for polish, latin in polish_to_latin.items():
        x = x.replace(polish, latin)
    return x

x = "ab   c   ee    jjj   "
print(delete_extra_spaces(x))
    