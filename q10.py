v = int(input())
w = int(input())
run = True
invalid = False
tw = v
fw = 0
while run:
    total = tw * 2 + fw * 4
    if total == w:
        run = False
        break
    if tw == 0:
        invalid = True
        break
    tw -= 1
    fw += 1

if not invalid:
    print(tw, fw)
else:
    print("invalid")

