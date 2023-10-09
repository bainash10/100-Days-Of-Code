#r - read mode (default when not specified mode)
#w - write mode
#a - append mode
#x - create mode
#t - shows how file is handled, opens file in text file
#b - shows how file is handled, opens file in binary file

# Reading A file
# f = open('Day49-File IO/myfile.txt', 'r') #opening a file
# print(f)
# text = f.read()
# print(text)
# f.close()

# f = open('Day49-File IO/myfile2.txt', 'a')
# f.write('Hello, World!')
# f.close()



#No need f.close()
with open('Day49-File IO/myfile.txt', 'a') as f:
   f.write("Nischal")

#Use of file to store datas in games and user data in programs