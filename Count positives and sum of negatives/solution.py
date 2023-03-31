def count_positives_sum_negatives(arr):
    c = 0
    s = 0
    resp = []
    if len(arr) != 0:
        for x in arr:
            if x > 0:
                c += 1
            else:
                s += x
        resp.append(c)
        resp.append(s)
    return resp
