pc = 0
mar = 0
mbr = 0
ir = 0
ibr = 0
ac = 0
mq = 0

''' "00000001" - LOAD M(X)
    "00000101" - ADD M(X)
    "00100001" - STOR M(X)
    "00000110" - SUB M(X)
    "00001001" - LOAD MQ,M(X)
    "00001011" - MUL M(X)
    "00001010" - LOAD MQ
    "00010100" - LSH
    "00010101" - RSH
'''

memory = []             #memory of the ias machine
for i in range(1000):
    memory.append(0)
    
'''def btod(binary):
    decimal=0
    for i in range(0,len(binary)):  
        j=binary[-i-1]              
        decimal=decimal+((2**i)*int(j))
    return decimal'''

def execute():
    global pc
    global mar
    global ibr
    global mbr
    global ir
    global ac
    global mq
    count = 0

    #fetch cycle begins
    mar = pc            
    mbr = memory[mar]
    ibr = mbr[20:]
    ir = mbr[0:8]
    mar = mbr[8:20]
    #fetch cycle ends

    #decoding and executing LHS
    if ir == "00000001":
        ad_dec = int(mar, 2)
        mbr = memory[ad_dec]
        ac = format(int(mbr, 2), '040b')

    if ir == "00100001":
        ad_dec = int(mar, 2)
        memory[ad_dec] = ac

    if ir == "00000101":
        ad_dec = int(mar, 2)
        mbr = memory[ad_dec]
        ac = format(int(ac, 2) + int(mbr, 2), '040b')

    if ir == "00000110":
        ad_dec = int(mar, 2)
        mbr = memory[ad_dec]
        ac = format(int(ac, 2) - int(mbr, 2), '040b')

    if ir == "00001001":
        ad_dec = int(mar,2)
        mbr = memory[ad_dec]
        mq = format(int(mbr, 2), '040b')

    if ir == "00001011":
        ad_dec = int(mar,2)
        mbr = memory[ad_dec]
        tmp = format(int(mq, 2) * int(mbr, 2), '080b')
        ac = tmp[0:40]
        mq = tmp[40:80]

    if ir == "00001010":
        ac = format(int(mq, 2), '040b')

    if ir == "00010100":
        ac = format(int(ac,2)*2, '040b')

    if ir == "00010101":
        ac = format(int(int(ac,2)*0.5), '040b')
        
    
    ir = ibr[0:8]
    mar = ibr[8:20]
    count = 1

    #decoding and executing RHS
    if ir == "00000101":
        ad_dec = int(mar, 2)
        mbr = memory[ad_dec]
        ac = format(int(ac, 2) + int(mbr, 2), '040b')

    if ir == "00000001":
        ad_dec = int(mar, 2)
        mbr = memory[ad_dec]
        ac = format(int(mbr, 2), '040b')

    if ir == "00100001":
        ad_dec = int(mar, 2)
        memory[ad_dec] = ac

    if ir == "00000110":
        ad_dec = int(mar, 2)
        mbr = memory[ad_dec]
        ac = format(int(ac, 2) - int(mbr, 2), '040b')

    if ir == "00001001":
        ad_dec = int(mar,2)
        mbr = memory[ad_dec]
        mq = format(int(mbr, 2), '040b')

    if ir == "00001011":
        ad_dec = int(mar,2)
        mbr = memory[ad_dec]
        tmp = format(int(mq, 2) * int(mbr, 2), '080b')
        ac = tmp[0:40]
        mq = tmp[40:80]

    if ir == "00001010":
        ac = format(int(mq, 2), '040b')

    if ir == "00010100":
        ac = format(int(ac,2)*2, '040b')

    if ir == "00010101":
        ac = format(int(int(ac,2)*0.5), '040b')


    pc = pc + 1
    
while True:
    choice = int(input("1.Addition of two numbers \n2.Subtraction of two numbers \n3.Sum of numbers in a list \n4.Area of Rectangle \n5.Sum of any Arithematic Progression \n6.Exit \nEnter choice:\n"))
    if choice == 1:
        a = int(input("Enter number 1:"))
        memory[100] = format(a, '040b')
        b = int(input("Enter number 2:"))
        memory[101] = format(b, '040b')

        memory[pc] = "00000001"+format(100, '012b')+"00000101"+format(101, '012b') #LOAD M(X),ADD M(X) 
        execute()
        memory[pc] = "00100001"+format(200, '012b')+"0"*20                         #STOR M(X)
        execute()

        print(int(memory[200], 2))
        print("\n")
    elif choice == 2:
        a = int(input("Enter number 1:"))
        memory[100] = format(a, '040b')
        b = int(input("Enter number 2:"))
        memory[101] = format(b, '040b')

        memory[pc] = "00000001"+format(100, '012b')+"00000110"+format(101, '012b')   #LOAD M(X), SUB M(X)
        execute()
        memory[pc] = "00100001"+format(200, '012b')+"0"*20                           #STOR M(X)
        execute()

        print(int(memory[200], 2))
        print("\n")
    elif choice == 3:
        li = eval(input("Enter a list of 10 elements:"))
        for i in range(10):
            memory[100+i] = format(li[i], '040b')
        
        
        memory[pc] = "00000001"+format(100, '012b')+"00000101"+format(101, '012b')   #LOAD M(X),ADD M(X)
        execute()
        memory[pc] = "00000101"+format(102, '012b')+"00000101"+format(103, '012b')   #ADD M(X), ADD M(X)
        execute()
        memory[pc] = "00000101"+format(104, '012b')+"00000101"+format(105, '012b')   #ADD M(X), ADD M(X)
        execute()
        memory[pc] = "00000101"+format(106, '012b')+"00000101"+format(107, '012b')   #ADD M(X), ADD M(X)
        execute()
        memory[pc] = "00000101"+format(108, '012b')+"00000101"+format(109, '012b')   #ADD M(X), ADD M(X)
        execute()
        memory[pc] = "00100001"+format(200, '012b')+"0"*20                           #STOR M(X)
        execute()

        print(int(memory[200], 2))
        print("\n")

    elif choice == 4:
        a = int(input("Enter length:"))
        memory[100] = format(a, '040b')
        b = int(input("Enter breadth:"))
        memory[101] = format(b, '040b')

        memory[pc] = "00001001"+format(100, '012b')+"00001011"+format(101, '012b')   #LOAD MQ,M(X), MUL M(X)
        execute()
        memory[pc] = "00100001"+format(200, '012b')+"00001010"+"0"*12                #STOR M(X), LOAD MQ
        execute()
        memory[pc] = "00100001"+format(201, '012b')+"0"*20                           #STOR M(X)
        execute()

        ans = memory[200]+memory[201]
        print(int(ans, 2))
        print("\n")


    elif choice == 5:
        a = int(input("Enter first element:"))
        d = int(input("Enter common difference:"))
        n = int(input("Enter number of terms you want to find the sum of:"))
        
        memory[100] = format(a, '040b')
        memory[101] = format(d, '040b')
        memory[102] = format(n, '040b')
        memory[103] = format(1, '040b')

        memory[pc] = "00000001"+format(102, '012b')+"00000110"+format(103, '012b')      #LOAD M(X), SUB M(X)
        execute()
        memory[pc] = "00100001"+format(200, '012b')+"00001001"+format(200, '012b')      #STOR M(X), LOAD MQ,M(X)
        execute()
        memory[pc] = "00001011"+format(101, '012b')+"00100001"+format(200, '012b')      #MUL M(X), STOR M(X)
        execute()
        memory[pc] = "00001010"+"0"*12+"00100001"+format(201, '012b')                   #LOAD MQ, STOR M(X)
        execute()
        memory[pc] = "00000001"+format(100, '012b')+"00010100"+"0"*12                   #LOAD M(X), LSH
        execute()
        memory[pc] = "00000101"+format(201, '012b')+"00100001"+format(202, '012b')      #ADD M(X), STOR M(X)
        execute()
        memory[pc] = "00001001"+format(102, '012b')+"00001011"+format(202, '012b')      #LOAD MQ,M(X), MUL M(X)
        execute()
        memory[pc] = "00100001"+format(203, '012b')+"00001010"+"0"*12                   #STOR M(X), LOAD MQ
        execute()
        memory[pc] = "00010101"+"0"*12+"00100001"+format(205, '012b')                   #RSH, STOR M(X)
        execute()

        print(int(memory[205], 2))
        print("\n")

    elif choice == 6:
        break
        

















    
    
    
