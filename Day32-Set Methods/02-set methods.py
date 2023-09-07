cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2)) #means seperate sets

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2)) #superset means if first set has another sets value pre existed
cities3 = {"Tokyo", "Madrid","Delhi"}
print(cities.issuperset(cities3))
print(cities3.issubset(cities))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
cities.discard("Tokyo2") #if used remove then error will be shown and further statements wont be run but discard() function will not throw error
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop() # removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. 
print(cities)
print(item)

'''cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities #Deletes cities and shows error
print(cities)'''

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear() #clears all the elements of set and prints empty set
print(cities)

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")