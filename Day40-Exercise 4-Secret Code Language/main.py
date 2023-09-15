name=input("Enter any character to change")
startingchar=name[0]

n=int(input("Press 1 for encoding and 0 for decoding"))
if(n==1):
#encoding
    if(len(name)>=3):
        enc="axg"+name[1:len(name)]+startingchar+"bai"
        print(enc)
    else:
        rev=name[::-1]#reversing the string
        print(rev) 

if(n==0):
#decoding
    #first need to encode
    if(len(name)>=3):
        enc="axg"+name[1:len(name)]+startingchar+"bai"
    else:
        rev=name[::-1]#reversing the string

    #decoding part
    if(len(name)>=3):
        print(startingchar+enc[3:len(enc)-4])
    else:
        print(rev[::-1]) #reversing the string
        