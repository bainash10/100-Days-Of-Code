ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}
#dictionaries are used in djangos and mongodb
#if you want to get updated with python the you can google "python documentation" and read you can skip some parts
ep1.update(ep2) #ep1 will get updated with value of ep2 also added in ep1 
#python dictionaries ordered with 3.70 and greater python version

#ep1.clear() #clears the dictionary ep1
#ep1.pop(122) #pops 122 key value pair -> desired item
#ep1.popitem() #pops last item of the dictionaries
#del ep1 #deletes ep1 and shows error when printed
#del ep1[122] #deletes ep1 dictionaries 122 key value pair
print(ep1)