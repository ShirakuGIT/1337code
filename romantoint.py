def romantoint(s):
    romandict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000

        }
    

    value = 0

    s = list(s)

    print(s)


    while len(s) != 0:


        if len(s) == 1 or romandict.get(s[0]) >= romandict.get(s[1]) :
            value += romandict.get(s[0])
            s.remove(s[0])

        elif romandict.get(s[0]) <= romandict.get(s[1]):
            value += romandict.get(s[1])-romandict.get(s[0])
            s.remove(s[0])
            s.remove(s[0])       
        
        elif len(s) == 1:
            value += romandict.get(s[0])
            s.remove(s[0])

   


    return value

print(romantoint("MCMLXXXVIII"))

