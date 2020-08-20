#!/usr/bin/env python3

# Python Object Oriented Programming by Joe Marini course example
# Using the __str__ and __repr__ magic methods


class Book(object):
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    # The __str__ function is used to return a user-friendly string
    # representation of the object
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # The __repr__ function is used to return a developer-friendly string
    # representation of the object
    def __repr__(self):
        return f"title={self.title},author={self.author},price={self.price}"

    # the __eq__ method checks for equality between two objects
    def __eq__(self, value):
        # if "value" is not an instance of "Book"
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to non-book type")

        return (self.title == value.title and
                self.author == value.author and
                self.price == value.price)

    # the __ge__ establishes >= relationship with another obj
    def __ge__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to non-book type")

        return self.price >= value.price

    # the __lt__ establishes <= relationship with another obj
    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to non-book type")

        return self.price < value.price

    # TODO: the __call__ method can be used to call the object like a function
    # changes the attributes of the object which were initially set during init
    def __call__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    """
    # __getattribute__ Called when an attribute is retrieved. Be aware that you can't
    # directly access the attr name otherwise a recursive loop is created
    # Calling the super class to avoid recursion
    
    Since we're already inside the function that's going to get called whenever an attribute value gets accessed, 
    we can't just refer to this object's attributes by name[object.attribute] because then this function will just 
    get recursively called over and over again and it will eventually crash. 
    
    So what we need to do is get the value of the current price by calling the superclass version of 
    __getattribute__.
    """

    def __getattribute__(self, attr_name):
        if attr_name == "price":
            p = super().__getattribute__("price")
            d = super().__getattribute__("_discount")
            return p - (p * d)
        return super().__getattribute__(attr_name)

    # __setattr__ called when an attribute value is set. Don't set the attr
    # directly here otherwise a recursive loop causes a crash
    def __setattr__(self, attr_name, value):
        if attr_name == "price":
            if type(value) is not float:
                raise ValueError("The 'price' attribute must be a float")
        return super().__setattr__(attr_name, value)

    # __getattr__ gets called when __getattribute__ lookup fails - you can
    # pretty much generate attributes on the fly with this method
    def __getattr__(self, name):
        return name + " is not here!"


if __name__ == "__main__":
    b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
    b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

    # print each object
    print(b1)
    print(b2)

    # use str() and repr()
    print(str(b1))
    print(repr(b2))

    b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
    b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
    b3 = Book("War and Peace", "Leo Tolstoy", 39.95)
    b4 = Book("To Kill a Mockingbird", "Harper Lee", 24.95)

    # Check for equality
    print(b1 == b3)
    print(b1 == b2)
    # print(b1 == 42)

    # Check for greater and lesser value
    print(b2 >= b1)
    print(b2 < b1)
    print(b3 >= b2)

    # Now we can sort them
    books = [b1, b3, b2, b4]
    books.sort()
    print([book.title for book in books])

    b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
    b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

    # call the object as if it were a function
    # and changes the attributes of Book b1
    print(b1)
    b1("Anna Karenina", "Leo Tolstoy", 49.95)
    print(b1)

    b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
    b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

    # Try setting and accessing the price
    b1.price = 38.95
    print(b1)

    b2.price = float(40)  # using an int will raise an exception
    print(b2)

    # If an attribute doesn't exist, __getattr__ will be called
    print(b1.randomprop)
