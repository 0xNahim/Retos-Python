def high_and_low(numbers):
    # ...
    numbers = numbers.split(" ")
    a = []
    for x in numbers:
        x = int(x)
        a.append(x)
    mayor = max(a)
    menor = min(a)
    numbers = str(mayor) + " " + str(menor)
    return numbers
