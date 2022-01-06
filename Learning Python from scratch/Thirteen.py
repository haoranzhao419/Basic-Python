def string(str1, str2):
    a = []
    b = []
    for i in str1:
        a.append(i)
    for i in str2:
        b.append(i)
    c = set()
    c.update(a)
    d = set()
    d.update(b)
    print(c | d)


string("115465032", "5591474")
