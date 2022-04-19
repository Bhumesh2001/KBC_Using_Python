import random
a = ["How many continents in the world?",
    "What is the capital of India?",
    "NG mei kaun se course padhaya jaata hai?",
    "who is author of the meghdoot?",
    "pongal is a popular festival of which state?",
    "which one of the following is essentially a solo dance?",
    "which of the following is a folk dance of india?",
    "who is the president of russia?",
    "which of the folllowing year was celebrated as the world communication year?",
    "which of following newspaper is 150 years old?",
    "The conark temple is dedicated to?","Van mahotsav was stated by?"]

b = [["1.Four", "2.Nine", "3.Seven", "4.Eight","5.life line"],
     ["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.New Delhi","5.life line"],
     ["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture","5.life line"],
     ["1.Vishakhadatta","2.Vlmiki","3.Banabatta","4.kalidas","5.life line"],
     ["1.karnataka","2.kerla","3.tamil nadu","4.Andhra pradesh","5.life line"],
     ["1.kuchipudi","2.kathak","3.mohiniattam","4.manipuri","5.life line"],
     ["1.kathkali","2.mohiniattam","3.garba","4.manipuri","5.life line"],
     ["1.joe biden","2.narendre modi","3.boris jhonson","4.vladimir putin","5.life line"],
     ["1.1981","2.1983","3.1985","4.1987","5.life line"],
     ["1.the statesjman","2.the times of india","3.the hindu","4.malayala manorma","5.life line"],
     ["1.vishnu","2.shiva","3.krishna","4.sun-god"],
     ["1.maharshi karve","2.bal gangadhar tilak","3.k m munshi","4.sanjay gandhi"]]

c = [3,4,1,4,3,3,3,1,2,2,4,3]
# life line.
t = ['1).50:50','2).Phone-a-Friend','3).Audience Poll','4).Switch the Question','5)gochi']
# 50:50 ke liye option
w = [["3.seven","4.eight"],["2.bhopal","4.new delhi"],["1.software engineering","2.counceling"],
     ["1.Vishakhadatta","4.kalidas"],["2.kerla","3.taml nadu"],["1.kuchiipudi","3.mohiniattam"],
     ["3.garba","2.manipuri"],["1.joe biden","2.narendra modi"],["1.1981","2.1983"],
     ["2.the times of india","3.the hindu"],["2.shiva","4.sun god"]]
d = 100
ab = 0
ac = 0
ad = 0
ae = 0
af = 0
s = 0
h = 1
while h > 0:
    a1 = random.randint(1,101)
    a2 = random.randint(1,101)
    a3 = random.randint(1,101)
    a4 = random.randint(1,101)
    if a1 + a2 + a3 + a4 == 100:
        break
    else:
        h += 1
k = [0,1,2,3,4,5,6,7,8,9,10]      
for i in range(len(a)):
    print()
    print('\033[1m','This Question for',d,'rupees amount.','\033[0m')
    print()
    h = random.choice(k)
    k.remove(h)
    if i == 10:
        break
    print('\033[1m','\033[91m','Q',str(i+1),a[h],'\033[0m')
    print()
    for j in b[h]:
        print('\033[35m',j,'\033[0m')
    print()
    n = int(input("enter your answer: "))
    print()
    if n == 5:
        if ab == 1:
            print('\033[33m','allready use 50:50','\33[0m')
        if ac == 1:
            print('\033[33m','allready used phone a friends','\033[0m')
        if ad == 1:
            print('\033[33m','allready used audience poll','\033[0m')
        if ae == 1:
            print('\033[33m','allready used switch the question','\033[0m')
        if af == 1:
            print('\033[33m','allready used gochi','\033[0m')
        for j in t:
            print('\033[32m',j,'\033[0m')
        print()
        l = int(input("choose your option: "))
        # 50:50 
        if l == 1 and ab < 1:
            print('\033[32m','choose correct answer','\033[0m')
            print()
            for e in w[h]:
                print('\033[96m',e,'\033[0m')
            print()
            ab += 1
            t.remove("1).50:50")
            q = int(input(" enter your answer: "))
            n = q
        elif l == 2 and ac < 1:
            print('\033[33m','correct answear is....','\033[0m')
            print('\033[34m',c[h],'\033[0m')
            ac += 1
            t.remove('2).Phone-a-Friend')
            v = int(input("enter your answer:  "))
            n = v
        elif l == 3 and ad < 1:
            print()
            if a1 + a2 + a3 + a4 == 100:
                print('\033[34m','1.Audience',a1,'% ','\033[0m')
                print('\033[34m','2.Audience',a2,'% ','\033[0m')
                print('\033[34m','3.Audience',a3,'% ','\033[0m')
                print('\033[34m','4.Audience',a4,'% ','\033[0m')
            print()
            ad += 1
            t.remove('3).Audience Poll')
            z = int(input('enter your answer: '))
            n = z     
        elif l == 4 and ae < 1:
            h = 11
            print('\033[31m',"Q.",str(i+1),a[h],'\033[0m')
            print()   
            for j in b[h]:
                print('\033[34m',j,'\033[0m')
            print()
            n = int(input("enter your answer: "))
            print()
            ae += 1
            t.remove('4).Switch the Question')
        s += 1
        if c[h] == n:
            d += d * 2
            print('\033[31m','you win amount',d,'rs.','\033[0m')
        print()
    if c[h]== n:
       print('\033[33m','congratulation,you win.','\033[0m')
       d += d * 2
       print()
       print('\033[32m','you win',d,'rs.','\033[0m')
       continue
    else:
        print('\033[32m','your answer is wrong \n you loss','\033[0m')
    print('\033[31m','do you want play continue y or n','\033[0m')
    print()
    m = input("enter your choice: ")
    if m == "y":
        i = 0
        continue
    else:
        break
print("your total amount is ",d,"rupees")

