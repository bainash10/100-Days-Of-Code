letter = "hey my name is {} and I am form {}"
continent = "ASIA"
name = "Nischal"
letter2 = "hey my name is {1} and I am form {0}"
print(letter.format(name,continent))
print(letter.format(continent,name))
print(letter2.format(continent,name))
#These are string Formatting

# Now for f-string -> use curly braces
#To print name as it is need to keep {{name}} use double curly braces
print(f"hey my name is {name} and I am form {continent}")
print(f"hey my name is {{name}} and I am form {{continent}}")


txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49.009999))

price = 49.009999
txt = f"For only {price:.2f} dollars!"
print(txt)

print(type(f"{2*30}"))
