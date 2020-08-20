class Student(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def email(self):
        return f'{self.first_name.lower()}.{self.last_name.lower()}@email.com'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @full_name.setter
    def full_name(self, name):
        first_name, last_name = name.split(' ')
        self.first_name = first_name
        self.last_name = last_name

    @full_name.deleter
    def full_name(self):
        print('Delete Name!')
        self.first_name = None
        self.last_name = None


if __name__ == "__main__":
    student = Student('Ronnie', 'Joshua')
    student.full_name = "Ronnie Joshua"

    print(student.first_name)
    print(student.email)
    print(student.full_name)

    del student.full_name
