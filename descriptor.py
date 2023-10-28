"""
A Python descriptor is a special type of object attribute that allows you 
to customize how attribute access is handled within a class. 
Descriptors are often used to define custom behavior for getting, 
setting, or deleting attributes in an object. 
They are typically implemented as classes with special methods 
such as __get__, __set__, and __delete__.

Descriptors provide a way to "describe" how 
attribute access should work for a particular object or class.
"""

class DescriptorExample:
    def __get__(self, instance, owner):
        if instance is None:
            return self  # Accessing the descriptor from the class itself
        return instance._value

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Value cannot be negative")
        instance._value = value

    def __delete__(self, instance):
        del instance._value

class MyClass:
    def __init__(self, value):
        self._value = value

    # Using the descriptor for the 'value' attribute
    value = DescriptorExample()

# Creating an instance of MyClass
obj = MyClass(42)

# Using the descriptor to get and set the 'value' attribute
print(obj.value)  # Calls DescriptorExample.__get__ to retrieve the value
obj.value = 10    # Calls DescriptorExample.__set__ to set the value
print(obj.value)  # Calls DescriptorExample.__get__ again
