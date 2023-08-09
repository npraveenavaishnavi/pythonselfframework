#class are user defined blueprint or prototype
#If we wrap the (def functions) inside the class then it is called as methods.
#self keyword is mandatory for calling variable names into method
#constructor name should be__ init__
#instance and class variables have whole different purpose
#new keyword is not required when you create object

class Calculator:
    num=100
# default constructor
    def __init__(self, a, b):
        self.FirstNumber=a
        self.SecondNumber=b
        print("I am called automatically when objects is created")

    def getData(self):
        print("I am now executing as method in class")
    def Summation(self):
        return self.FirstNumber+self.SecondNumber+self.num

obj = Calculator(2,3)       #syntax to create objects in python
obj.getData()               #To call the method present in the class
print(obj.Summation())      #To call the variable in the class

obj1= Calculator(5,8)
obj.getData()
print(obj1.Summation())