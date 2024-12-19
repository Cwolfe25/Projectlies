import random
numb = 9
setnumb = 9
numb1 = numb - 1
lst = []
while numb >0 :
    temp = random.randint(-1000000000000,10000000000000)
    temp = int(temp)
    lst.append(temp)
    numb = numb - 1
while numb1 >=0:
    nextnumb = 20
    while nextnumb >0:
        print(lst)
        a = lst[numb1]
        numb2 = random.randint(0,8)
        numb3 = random.randint(0,8)
        numb4 = random.randint(0,8)
        check1 = 0
        check2 = 0
        check3 = 0
        while check1 ==0:
            if numb1 == numb2 or numb3 == numb2 or numb4 == numb2:
                numb2 = random.randint(0,8)
            else:
                check1 = 1
        while check2 ==0:
            if numb1 == numb3 or numb2 == numb3 or numb4 == numb3:
                numb3 = random.randint(0,8)
            else:
                check2 = 1
        while check3 ==0:
            if numb1 == numb4 or numb2 == numb4 or numb4 == numb3:
                numb4 = random.randint(0,8)
            else:
                check3 = 1
        b = lst[numb2]
        c = lst[numb3]
        d = lst[numb4]
        account = a + b - c -d
        if account / 20 == int(account/20):
            print("set works")
            numb1 = -100
        nextnumb = nextnumb+1
        

    


    

