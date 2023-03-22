def abbrev_name(name):
    
    abbv = ""
    c=1
    for l in name:
        if l == name[0] and c ==1:
            abbv += l.upper()
            c -=1
        elif l == " ":
            abbv += "."+ name[name.find(l)+1].upper()
    return abbv
