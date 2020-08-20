#!/usr/bin/env python3

# Understanding class inheritance


class Publication(object):
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Periodical(Publication):
    def __init__(self, title, price, publisher, period):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher


class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages


class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, publisher, period)


class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, publisher, period)


# Understanding multiple inheritance


class A(object):
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "Class A"


class B(object):
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "Class B"


class C(B, A):
    def __init__(self):
        super().__init__()

    def show_properties(self):
        print(self.foo)
        print(self.bar)
        print(self.name)


class D(A, B):
    def __init__(self):
        super().__init__()

    def show_properties(self):
        print(self.foo)
        print(self.bar)
        print(self.name)


if __name__ == "__main__":
    # create the class and call showname()
    c = C()
    print(C.__mro__)
    c.show_properties()

    d = D()
    print(D.__mro__)
    d.show_properties()
