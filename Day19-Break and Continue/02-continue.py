print("Out of Loop")
print("\n\n")
for i in range(12):
    if(i == 10):
        print("Skip the Iteration")
        continue #means skipping the iteration of that condition
    print("5 X", i+1,"=",5 * (i+1))