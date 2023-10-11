#seek and tail functions examples
'''with open('Day51-seek and tail functions/file.txt', 'r') as f:
  print(type(f))
  # Move to the 10th byte in the file ->Space also counted, start counting from 1 - ....
  f.seek(10)

  print(f.tell()) #Returns where the cursor is right now
  # Read the next 5 bytes
  data = f.read(7)
  print(data)'''

#truncate example
with open('sample.txt', 'w') as f:
  f.write('Hello World!')
  f.truncate(5) #Only Hello will be written as truncate functions limits the size of word to be written in file

with open('sample.txt', 'r') as f:
  print(f.read())


