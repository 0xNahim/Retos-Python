def dna_to_rna(dna):
    arn = ""
    for i in dna:
        if i == "T":
            i = "U"
        arn += i
    return arn
