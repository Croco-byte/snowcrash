cypher = "cdiiddwpgswtgt"

for i in range(0,20) :
    print("[*] i is " + str(i))
    result = ""
    for c in cypher :
        j=0
        y=ord(c)
        while (j < i) :
            y += 1
            if (y == 123) :
                y = 97
            j += 1
        result += chr(y)

    print("[+] " + result)
