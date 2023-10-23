import random #importing random module to use its functions
 
def check(comp, user):  #to check between computer and user and return a number
  if comp == user:
    return 0 #draw
    
  if(comp == 0 and user ==1):
    return -1 #you lose
    
  if(comp == 1 and user ==2):
    return -1 #you lose
    
  if(comp == 2 and user == 0):
    return -1 #you lose

  return 1 #otherwise return 1 that means you win: user wins
    
  
comp = random.randint(0, 2) #inside comp variable random integer from 0,1,2 is assigned
user = int(input("0 for Snake, 1 for water and 2 for Gun:\n"))

score = check(comp, user) 

print("You: ", user)
print("Computer: ", comp)

if(score == 0):
  print("Its a draw")
elif (score == -1):
  print("You Lose")
else:
  print("You Won")
  


