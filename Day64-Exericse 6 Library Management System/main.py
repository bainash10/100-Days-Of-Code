class Library:
    no_of_books=0  #Initialiaze Class Var
    def __init__(self, b):
        Library.no_of_books+=1 #Incrementing class variable
        self.books=[]
        self.books.append(b) #Add book to list
        
no=int(input("How many books to add"))

while(no!=0):
    name=input("Enter the name of book to add to the Library")
    bk=Library(name)
    print("No of books:", bk.no_of_books)
    print("Books:",bk.books)
    print("*----------------------------*")
    no-=1




    
