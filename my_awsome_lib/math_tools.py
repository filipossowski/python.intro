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

def mean(tab):
    if len(tab) == 0:
        print("Empty list.")
        return False
    else:
        return sum(tab)/len(tab)


x= []
print(mean(x))