#Object oriented programming is when you create your own custom class.
#One reason you should do this is that is saves you time.
#Another reason is it makes calling certain functions easier with tkinter
#Another reason is that it makes your code more readable.
#Another reason is that it makes your code more organized.
#Another reason is that it makes your code more efficient.


class Dog:              #
#init creates certain parameters that allow you to define information quickly.
    def __init__(self, name): #
        self.name = name
    
    def get_name(self):
	    return self.name
    
if __name__ == "__main__":
    d = Dog(str(input("Name your dog: ")))
    print(d.get_name())
