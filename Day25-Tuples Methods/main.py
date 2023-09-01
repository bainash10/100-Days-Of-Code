# countries = ("Spain", "Italy", "India", "England", "Germany")
# temp = list(countries)
# temp.append("Russia")       #add item 
# temp.pop(3)                 #remove item
# temp[2] = "Finland"         #change item
# countries = tuple(temp)
# print(countries)

# countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
# countries2 = ("Vietnam", "India", "China")
# southEastAsia = countries + countries2
# print(southEastAsia)

tup = (1,2,3,4,5,6,7,8,3,4,5,6)
print(tup.count(2))
print(tup.index(2)) #2 first occurence index
print(tup.index(4,2,8))
print(len(tup))

#to make changes in tuple first convert to list then manipulate and again keep back to tuple

