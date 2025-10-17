#Make a Book class that takes title and author in its constructor and prints a message like "Book: Title by Author".

# class Book:
#     def __init__(self, title, author):        
#         self.title = title
#         self.author = author

#     def info(self):
#         print(f"Book : {self.title} by {self.author}")

# Comic = Book("Marvel", "Stan Lee")

# Comic.info()

#Create a Rectangle class with attributes length and width. Add a method to calculate area and perimeter.
# class Rectangle():
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth
    
#     def info(self):
#         area = self.length * self.breadth
#         perimeter = 2*(self.length + self.breadth)
#         print(f"The area of the Rectangle is {area} \nThe perimeter of the Rectangle is {perimeter}")

# a = Rectangle(10, 5)
# a.info()

#Create a BankAccount class with attributes account_number, balance. Add methods deposit() and withdraw()
# class BankAccount():
#     def __init__(self, ac_no, bal):
#         print("Welcome to xyz bank")
#         self.account_number = ac_no
#         self.balance = bal

#     def info(self):
#         print(f"Dear Customer,\nYour account number : {self.account_number} with a Balance of {self.balance} dollars")

#     def deposit(self):
#         deposit_amount = int(input("How much would you like to Deposit:"))
#         self.balance = self.balance + deposit_amount
#         print(f"Dear Customer,\nYour account number : {self.account_number} with a Balance of {self.balance}")

#     def withdraw(self):
#         withdraw_amount = int(input("How much would you like to Withdraw:"))
        
#         if withdraw_amount <= self.balance:
#             self.balance = self.balance - withdraw_amount
#             print(f"Dear Customer,\nYour account number : {self.account_number} with a Balance of {self.balance}")
#         else:
#             print("Insufficent Balance")

# a = BankAccount(1234, 50000)

# a.info()
# # a.deposit()
# a.withdraw()
        
#Write a Laptop class with attributes brand, ram, and price. Add a method apply_discount(percent) to reduce the price.

# class Laptop:
#     def __init__(self, brand, ram, price):
#         self.brand = brand
#         self.ram = ram
#         self.price = price

#     def info(self):
#         print(f"This is {self.brand}'s new laptop with {self.ram} GB ram, launching at {self.price} dollars")
    
#     def apply_discount(self):
#         discount_percentage = int(input("Enter the coupon discount: "))

#         discount_price = self.price*(discount_percentage/100)
#         self.price = self.price - discount_price

#         print(f"On applying {discount_percentage}% discount, revised price for the laptop is {self.price} ")

# a = Laptop("Asus", 16, 50000)
# a.info()
# a.apply_discount()
    
#Create an Employee class with attributes name, salary, and department. Add a method to give a raise.

class Employee:
    def __init__(self, name, salary, dept):
        self.name = name
        self.salary = salary
        self.dept = dept

    def info(self):
        print(f"{self.name} from {self.dept} department earns {self.salary} dollars")
    
    def hike(self):
        hike_perc = int(input("Enter hike percentage: "))
        hiked_number = self.salary*(hike_perc/100)
        self.salary = round(self.salary + hiked_number)

        print(f"Congratulations!! You {hike_perc}% raise and now your salary is {self.salary} dollars")

a = Employee("Sam", 8000, "Forensic")

a.info()
a.hike()

#Build a ShoppingCart class where you can add_item(item, price) and total_cost().

# class ShoppingCart:
#     def __init__(self):
#         self.items = []

#     def add_item(self, item, price) :
#         self.items.append((item, price))
#         print(f"Added {item} for Rs {price}")

#     def total_cost(self):
#         total = sum(price for _, price in self.items)
#         return total



# a = ShoppingCart()
# a.add_item("Milk", 74)
# a.add_item("Coffee", 26)
# print("Total: Rs", a.total_cost())


#Make a Movie class with title, genre, and rating. Add a method to check if the movie is a "Hit" if rating > 8.

# class Movie:
#     def __init__(self, title, genre, rating):
#         self.title = title
#         self.genre = genre
#         self.rating = rating
    
#     def info(self):
#         print(f"{self.title} is a {self.genre} movie with a rating of {self.rating}")
        
#     def hit(self):
#         if self.rating > 8:
#             print("This movie was a hit one")
#         else:
#             print("It's not a hit")

# a = Movie("Source code", "Thriller", 9)
# b = Movie("Funny people", "Comedy", 7)

# a.info()
# a.hit()
# b.info()
# b.hit()

#Create a Library class that manages a list of Book objects. Add methods to add_book() and show_books().

class Book:
    def __init__(self, title, author):        
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book.title} by {book.author}")

    def show_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author}")

lib = Library()
lib.add_book(Book("Encyclopedia", "John Harris"))
lib.add_book(Book("GOT", "George R.R. Martin"))
lib.add_book(Book("Marvel Comic", "Stan Lee"))
lib.add_book(Book("Pursuit of happiness", "Chris Gardener"))

lib.show_books()