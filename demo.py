import sys 
for line in sys.stdin:
# line = '2 123456789 abc'
    a = line.split()
    n = int(a[0])
    l = a[1:]
    arr = []
    for i in l:
        while len(i) > 8:
            arr.append(i[:8])
            i = i[8:]
        arr.append(i+'0'* (8 - len(i)))
    arr.sort()
    for i in arr:
        print(i, end=' ')