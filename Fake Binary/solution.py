def fake_bin(x):
    y = ""
    for i in x:
        if int(i) >= 5:
            i = "1"
        elif int(i) < 5:
            i = "0"
        y += i
    return y
