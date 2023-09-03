listofquestions = ["Full form of HTML","Full form of CSS", "Full form of ISP", "Most Used Programming Language", "Which one is Input Device"]
answer0 = ["Hypertext Markup Language","Hypertext Markup Lang","Hypertext Mark Language","Hypertext "]
answer1 = ["Cascading", "Cascading Style Sheets", "Styling", "Cascade"]
answer2= ["Internet Service Provider", "Internet", "Service", "Provider"]
answer3= ["JS","PHP","C","C++"]
answer4= ["Keyboard", "Airpods", "Monitor", "Speaker"]

print(listofquestions[0])
print(answer0)
ans=int(input("choose answer 0,1,2 or 3"))
if(ans==0):
     a=500
     print("You won 500$")
else:
    a=0
    print("Your Balance is",a)
    

print(listofquestions[1])
print(answer1)
ans=int(input("choose answer 0,1,2 or 3"))
if(ans==1):
     a=1000
     print("You won 1000$")
else:
    a=500
    print("Your Balance is",a)

print(listofquestions[2])
print(answer2)
ans=int(input("choose answer 0,1,2 or 3"))
if(ans==0):
     print("You won 1500$")
else:
    a=800
    print("Your Balance is",a)

print(listofquestions[3])
print(answer3)
ans=int(input("choose answer 0,1,2 or 3"))
if(ans==0):
     print("You won 2000$")
else:
    a=1000
    print("Your Balance is",a)

print(listofquestions[4])
print(answer4)
ans=int(input("choose answer 0,1,2 or 3"))
if(ans==0):
     print("You won 2500$")
else:
    a=1100
    print("Your Balance is",a)

