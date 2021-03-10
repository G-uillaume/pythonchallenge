
def distance(a, b):
    a = a.lower()
    b = b.lower()
    c = 0

    try:
        assert len(a) == len(b)

        for i in range(len(a)):
            if a[i] != b[i]:
                c += 1
        
    except AssertionError:
        return "Strings must be the same length!"
    
    return c