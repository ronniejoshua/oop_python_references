#!/usr/bin/env python3

# Using data classes to represent data objects

from dataclasses import dataclass, field
import random


def price_func():
    return float(random.randrange(20, 40))


@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0
    price: float = field(default_factory=price_func)

    # the __post_init__ function lets us customize additional properties
    # after the object has been initialized via built-in __init__
    def __post_init__(self):
        self.description = f"{self.title} by {self.author}, {self.pages} pages"

    # You can define methods in a dataclass like any other
    def book_info(self):
        return f"{self.title}, by {self.author}"


# "The "frozen" parameter makes the class immutable
@dataclass(frozen=True)
class ImmutableClass:
    value_one: str = "Value 1"
    value_two: int = 0

    # Frozen classes can't modify themselves either
    def some_func(self, new_val):
        # 'ImmutableClass' object attribute 'value_one' is read only
        self.value_one = new_val


if __name__ == "__main__":
    # create some instances
    b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
    b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

    # access fields
    print(b1.title)
    print(b2.author)

    # print the book itself - dataclasses provide a default
    # implementation of the __repr__ function
    print(b1)

    # comparing two dataclasses
    b3 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
    print(b1 == b3)

    # change some fields, call a regular class method
    b1.title = "Anna Karenina"
    b1.pages = 864
    print(b1.book_info())

    # create some Book objects
    b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
    b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

    # use the description attribute
    print(b1.description)
    print(b2.description)

    # Create a default book object
    b1 = Book()
    print(b1)

    # Create a specified book, price is set by field operator
    b1 = Book("War and Peace", "Leo Tolstoy", 1225)
    b2 = Book("The Catcher in the Rye", "JD Salinger", 234)
    print(b1)
    print(b2)

    obj = ImmutableClass()
    print(obj.value_one)

    # attempting to change the value of an immutable class
    # throws an exception
    # obj.value_one = "Another value"
    # print(obj.value_one)

    # Frozen classes can't modify themselves either
    obj.some_func(20)
