#in python if called object then it is dictionary 
#in python if called array it is called list
questions=[
    ["Which lang was used to create fb?", "Python", "JS", "PHP","NONE",4],
    ["Which lang was used to create fb?", "Python", "JS", "PHP","NONE",4],
    ["Which lang was used to create fb?", "Python", "JS", "PHP","NONE",4],
    ["Which lang was used to create fb?", "Python", "JS", "PHP","NONE",4],
    ["Which lang was used to create fb?", "Python", "JS", "PHP","NONE",4],
    ["Which lang was used to create fb?", "Python", "JS", "PHP","NONE",4]
]

levels=[1000,2000,3000, 5000, 10000,100000]
money = 0

i=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"Question for Rs. {levels[i]}")
    print(f"a. {question[1]}     b. {question[2]}")
    print(f"c. {question[4]}     d. {question[4]}")
    reply=int(input("Enter your ans 1-4 or 0 to quit"))
    if(reply==0):
        money = levels[i-1]
        break
    if(reply==question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if(i==4):
            money = 10000
        elif(i==9):
            money=32000
        elif(i==14):
            money=10000000
    else:
        print("Wrong answer!")
        break
print(f"Your take home money is {money}")