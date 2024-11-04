#Break statement - Exits ana entire loop

num=20
while num<=25:
    print(num)
    if num==23:
        break
    num+= 1

#Continue statement- skips a loop
devices=["laptop", "phones", "tablets"]
for x in devices:
    if x == "phones":
        continue
    print(x)