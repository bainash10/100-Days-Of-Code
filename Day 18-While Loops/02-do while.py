#exit controlled loop
# most common technique to emulate a do-while loop is to use an infinite while loop with a break statement wrapped in an if statement that checks a given condition and breaks the iteration if that condition becomes true.
while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break