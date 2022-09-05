
lister= ["A","B","C","D","E"]
for r in (6):
    for c in range(6):
        if(r==c):
            elem= lister[r-1]
        else:
           elem = "-"
        print(elem)
    print()

