t="FPT"

d=t.split(',')

print(len(d))

def test1():
    print("DA THUC HIEN 1")
def test2():
    print("DA THUC HIEN 2")
def test3():
    print("DA THUC HIEN 3")
i=0
for i in range(len(d)):
    print(d[i])
    if d[i]=='TGDD':
        test1()
    elif(d[i]=='FPT'):
        test2()
    elif(d[i]=='cellphones'):
        test3()
    else:
        print("Khong co")
