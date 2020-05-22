
# Polymorphism

Polymorphism means having many forms. In programming, polymorphism means same function name(but different signatures) being used for different types.

Example of inbuilt polymorphic functions:

```python
# len() being used for a string
print(len("polymorphism")

# len() being used for a list
print(len([10, 20, 30]))
```

## Polymorphism with class methods

Below code shows how python can use two different class types, in the same way. We create a for loop that iterates through a tuple of objects. Then call the methods without being concerned about which class type each object is. We assume that these methods actually exists in each class.

```python
class India():
    def capital(self):
        print("New Delhi is the capital of India")
      
    def language(self):
        print("Hindi is the primary language of India")
        
    def type(self):
        print("India is a developing country")
        
class USA():
    def capital(self):
        print("Washington D.C is the capital of USA")
      
    def language(self):
        print("English is the primary language of USA")
        
    def type(self):
        print("USA is a developed country")
    
obj_ind = India()
obj_usa = USA()

for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()
    
```
Output:

New Delhi is the capital of India.

Hindi the primary language of India.

India is a developing country.

Washington, D.C. is the capital of USA.

English is the primary language of USA.

USA is a developed country.




```python

```
