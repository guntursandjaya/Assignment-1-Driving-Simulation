abc = input().upper()
p = [1,0,0]
for w in abc:
    if w == 'A':
        p[0],p[1] = p[1], p[0]
    elif w == 'B':
        p[1], p[2] = p[2], p[1]
    elif w == 'C':
        p[0], p[2] = p[2], p[0]
if p == [1,0,0]:
    print("1")
elif p == [0,1,0]:
    print("2")
elif p == [0,0,1]:
    print("3")
