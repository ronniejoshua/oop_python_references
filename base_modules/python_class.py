#!/usr/bin/env python3


class Book(object):
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    # TODO: double-underscore properties are hidden from other classes
    __booklist = None

    # class methods receive a class as their argument and can only
    # operate on class-level data
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, pages, author, price, booktype):
        self.title = title
        self.pages = pages
        self.author = author
        self.price = price
        self.__name_mangling = "This is name mangling in Python"
        if booktype not in Book.BOOK_TYPES:
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype
        # suppose to be an internal attribute
        self._discount = None

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, newtitle):
        self.title = newtitle

    # instance methods are defined like any other function, with the
    # first argument as the object ("self" is just a convention)
    def set_discount(self, amount):
        self._discount = amount

    def get_price(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    # static methods do not receive class or instance arguments
    # and usually operate on data that is not instance- or
    # class-specific
    @staticmethod
    def getbooklist():
        if Book.__booklist is None:
            Book.__booklist = []
        return Book.__booklist
