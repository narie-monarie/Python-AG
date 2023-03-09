x = 5
name = "Ryan"
print(type(name))
print(x)

# Lists

my_list = [1, 2, 3, 4, 5]
my_list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
my_list1[0].append(12)
print(my_list1)
print(len(my_list1))

# Sets

my_set = {1, 2, 3, 4, 5, 1}
print(my_set)


# Tuples
my_tuple = (1, 2, 3)  # Cannot append or add
print(len(my_tuple))

# Dictionary

my_dictionary = {1: "Hello", 2: "World"}
print(my_dictionary[1])

# control flow

age = 10

if age > 12:
    print("Hello")
else:
    print("NO")


# For Loops

a = [1, 2, 3]

for i in a:
    print(i)

# Functions


def hello(n):
    print("Hello " + n)


hello("mama")


# Classes

class Dog:
    def __init__(self, name):
        self.name = name
        self.legs = 4

    def speak(self):
        print(self.name + " says Bark")


my_dog = Dog("Rover")
another_dog = Dog("Fluffy")
my_dog.speak()
another_dog.speak()
