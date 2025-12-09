def is_palindrome(text):
    t = text.lower().replace(' ', '')
    if t == t[::-1]:
        return True
    else:
        return False
    
def delete_extra_spaces(text):
    return ' '.join(text.split())



    