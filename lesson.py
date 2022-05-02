class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        

    def greeting(self):
        print('Hey there! My name is {first_name} and im {age} years old'.format
        (first_name=self.first_name, age=self.age))
    
    def birthday(self):
        self.age += 1

class Student(Person):
    def __init__(self, first_name, last_name, age, grade):
        super().__init__(first_name, last_name, age)
        self.grade= grade
    
    def greet_class(self):
        print('Hi my name is {first_name} and im in {grade} grade'.format(
            first_name=self.first_name, grade=self.grade
        ))

# Creating an INSTANCE of Person

my_person = Person('GJ', 'Haaland', 32)
my_person.greeting()
my_student = Student('GJ', 'Haaland', 32, '17th')
my_student.greet_class()
#print(my_person.first_name + ' ' + my_person.last_name)