

# Object-Oriented Python

Class lets us bundle behaviour and state together in an object.
- Behavior : function
- State    : variables

To use a class, we can create an object from it. This is known as Object instantiation.

- When we create objects from a class, each object shares the class's coded methods, but maintains its own copy of varaibles.
- The first argument to every method is always "self" and its value is supplied by the interpreter


```python
# Example
class CountFromBy:
    def increase(self) -> None:
        self.val += self.incr
```

- "self" is assigned the current object by the interpreter when a method is invoked, and that the interpreter expects each method's first argument to take this into account.

- Overriding is altering or replacing a method of the superclass with a new method(with the same name) in the subclass. No special syntax is needed to do this; the subclass's newly created method is automatically called instead of the superclass's method.

- super() function returns the object as an instance of the parent class, allowing us to call the parent method directly

- Multiple inheritance : A subclass that inherits from more than one parent class is able to access functionality from both of them. The simplest and the most useful form of multiple inheritance is called a mixin. A mixin is generally a superclass that is not meant to exists on its own, but is meant to be inherited by some other class to provide extra functionality.
