class Book:
    def __init__(self,title,author,price,pages,p_year):
        self.title = title
        self. author =  author
        self.price = price
        self.pages = pages
        self.publication_year = p_year

b1 = Book("Wings of Fire", "A. P. J. Abdul Kalam", 350, 180,2020)

b2 = Book("The God of Small Things", "Arundhati Roy", 400, 340,2010)

b3 = Book("Shyamchi Aai", "Sane Guruji", 200, 250,2002)

print(b1.title)
print(b1.author)
print(b1.price)
