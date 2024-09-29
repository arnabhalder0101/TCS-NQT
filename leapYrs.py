n1 = int(input('start: '))
n2 = int(input('end: '))

for yr in range(n1, n2 + 1):
    lpYr = True
    if yr % 4 == 0 and (yr % 400 == 0 or yr % 100 != 0):
        lpYr = True
    else:
        lpYr = False

    if lpYr:
        print(yr, end=' ')