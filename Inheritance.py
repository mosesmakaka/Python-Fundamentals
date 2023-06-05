#Inheritance in Python

class Person: # define Person class
    def __init__(self, personName): # constructor  
        self.name = personName  # instance variable

    def showName(self):        # method
        print(self.name)   # instance variable
        
"""
A simple class example.
Person class specific. This is a class variable. 
It is shared by all instances of this class. 
It is accessed as Person.name from inside the class and as person1.name from outside the class.
"""

class Student(Person): 				# Student inherits from Person superclass
    studentClass = ""                  # Student class specific

    def __init__(self, studentName, studentClass):  # constructor
        Person.__init__(self, studentName)		# superclass constructor
        self.studentClass = studentClass  		# Student class specific

    def getStudentClass(self):        # method
        return self.studentClass   # instance variable

person1 = Person("Dave")           # create Person object
person1.showName()                  # Dave
student1 = Student("Mary", "Maths") # create Student object
print(student1.getStudentClass())   # Maths
student1.showName()                 # Mary
print(student1.name)                # Mary
#print(person1.studentClass)         # AttributeError: 'Person' object has no attribute 'studentClass' so to avoid this we use inheritance.