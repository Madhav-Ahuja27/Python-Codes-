class Library:
  def __init__(self,n,no,bs):
    self.name=n
    self.no_of_books=no
    self.books=bs
  def printallbooks(self):
    print(f"The books of the {self.name} are {self.books}")
  def addbook(self,newbook):
    self.books.append(newbook)
  def numbooks(self):
    print(f"The number of books of {self.name} are {self.no_of_books}")

shelf1=Library("First shelf",3,['harry','peter','mary'])
shelf1.printallbooks()
shelf1.addbook('miles')
shelf1.printallbooks()
shelf1.numbooks()
