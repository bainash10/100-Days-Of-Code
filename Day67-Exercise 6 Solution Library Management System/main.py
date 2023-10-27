class Library:
  def __init__(self):
    self.noBooks = 0 #assigning 0 to no of books
    self.books = []  #empty list
    
  def addBook(self, book):
    self.books.append(book) #appending books in the list
    self.noBooks = len(self.books)

  def showInfo(self):
    print(f"The library has {self.noBooks} books. The books are")
    for book in self.books:
      print(book)


l1 = Library()  #creating object
l1.addBook("Harry Potter1")
l1.addBook("Harry Potter2")
l1.addBook("Harry Potter3")
l1.showInfo()
    
  