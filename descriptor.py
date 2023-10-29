"""
A Python descriptor is a special type of object attribute that allows you 
to customize how attribute access is handled within a class. 
Descriptors are often used to define custom behavior for getting, 
setting, or deleting attributes in an object. 
They are typically implemented as classes with special methods 
such as __get__, __set__, and __delete__.

Descriptors provide a way to "describe" how 
attribute access should work for a particular object or class.

In Python, descriptors are objects that define one or more of the following special methods:

__get__(self, instance, owner): This method is called when 
you access the descriptor as an attribute of an object. 
It describes how to get the value of the attribute.

__set__(self, instance, value): This method is called when you assign a value 
to the descriptor as an attribute of an object. 
It describes how to set the value of the attribute.

__delete__(self, instance): This method is called when you delete 
the descriptor as an attribute of an object. 
It describes what happens when you delete the attribute.
"""
class IntegerAttribute:
    def __get__(self, instance, owner):
        return instance._value

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError("Age must be an integer")
        instance._value = value

    def __delete__(self, instance):
        del instance._value

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    age = IntegerAttribute()  # Using the descriptor for age

# Creating instances of Person
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Setting the age attribute with valid and invalid values
person1.age = 35  # Valid: Age is an integer
try:
    person2.age = "25"  # Invalid: Age is not an integer
except ValueError as e:
    print(e)  # Output: "Age must be an integer"

# Accessing the age attribute
print(person1.age)  # Output: 35
print(person2.age)  # Output: 25

# Deleting the age attribute
del person1.age
try:
    del person2.age  # Deleting a non-existent attribute raises an AttributeError
except AttributeError as e:
    print(e)  # Output: "'Person' object has no attribute '_value'"
