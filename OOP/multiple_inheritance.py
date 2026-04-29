class Person:
    def message(self):
        return "I am a person"

    def __str__(self):
        return self.message()

class Father(Person):
    def sub_message(self):
        return 'cool daddy'

    def __str__(self):
        return f"{self.message()} and {self.sub_message()}"

class Mother(Person):
    def sub_message(self):
        return 'awesome mom'
    
    def __str__(self):
        return f"{self.message()} and {self.sub_message()}"

class Child(Father, Mother):
    def sub_message(self):
        return 'I am the coolest kid'
    
    def __str__(self):
        return self.sub_message()

mom = Mother()
kid = Child()
print(kid)