dic = {
    12: "human being",
    13: "Object",
    "Baidar": "Nischal"

}
print(dic["Baidar"])
print(dic[12])

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
print(info['name']) #Throws error when key doesnt exist like name2
print(info.get('name')) #Doesnt throw error when key doesnt exist
print(info.keys()) #Prints keys 
print(info.values()) #Prints values

for key in info.keys():
    print(info[key])
    print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
    print(f"The value corresponding to the key {key} is {info[key]}")