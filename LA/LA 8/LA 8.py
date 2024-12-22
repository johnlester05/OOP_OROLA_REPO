class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def describe(self):
        pass
        
book1= Book("Ang kurimaw", "Peter ascovado")
book2 = Book("Torotot", "Gregor utoy")

print(f'''
Title: {book1.title}
Author: {book1.author}

Title: {book2.title}
Author: {book2.author}
''')
del book1.author
del book2.author

print(book1.author)
print(book2.author)
