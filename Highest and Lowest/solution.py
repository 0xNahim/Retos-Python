def high_and_low(numbers):
    # ...
    mayor = 0
    menor = 0
    numbers = numbers.split()
    for x in numbers:
        if int(x) > mayor and int(x) != 1:
            mayor = int(x)
        elif int(x) < menor or int(x) == 1:
            menor = int(x)
    numbers = str(mayor) + " " + str(menor)
    return numbers
