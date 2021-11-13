f = open("token","rb")
encoded = f.read()
result = ""
i = 0

for c in encoded :
    c -= i
    if (c > 0) :
        result += chr(c)
    i += 1

print(result)
