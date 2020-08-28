vas = 'dani:GSDGSSCVAXE:vasia'

new = ''
cnt = 0
ld = 4
lv = 5

for h in vas:
    new += h
    cnt += 1
    if ld > 4:
        new += ld
        cnt += 1


    print(new)
