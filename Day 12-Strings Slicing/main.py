names = "Nischal, Baidar"
print(names[0:7]) #from 0 to 7 i.e N to l prints
#for function square bracket for slicing square bracket 
print(len(names)) #gives length starting from 1 not 0

fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")
print(fruit[0:4]) 
#strng slicing function
#4 index wont be seen 
#including 0 but not 4
print(fruit[1:4]) #from 1
#including 1 but not 4
print(fruit[:4]) #automatically keeps 0
print(fruit[:]) #prints everything
print(fruit[0:-3])  #-3 === len(fruit)-3 automatically
print(fruit[0:len(fruit)-3])
print(fruit[-1:len(fruit)-3]) #prints nothing because 5-1=4 to 5-3=2
print(fruit[-3:-1]) #2:4

#Quick Quiz:
nm="Harry"
print(nm[-4:-2]) 
#here len = 5
#5-4=1 : 5-2=3 i.e 1:3 --> ar is the output