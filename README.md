

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

