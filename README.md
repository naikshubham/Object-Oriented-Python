
# Object-Oriented Python

Class lets us bundle behaviour and state together in an object.
- Behavior : function
- State    : variables

To use a class, we can create an object from it. This is known as Object instantiation.

- When we create objects from a class, each object shares the class's coded methods, but maintains its own copy of varaibles.
- The first argument to every method is always "self" and its value is supplied by the interpreter

#### Constructor
- Construction `__init__()` method is called every time an object is created.

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


```python
# Example
class Contact:
	#all_contacts = []
	all_contacts = ContactList()
	
	def __init__(self, name, email):
		self.name = name
		self.email = email
		#Contact.all_contacts.append(self)
		self.all_contacts.append(self)
        
 class MailSender:
	def send_mail(self, message):
		print("sending mail to " + self.email)
        
# multiple inheritance
class EmailableContact(Contact, MailSender):
	pass
```

The syntax for multiple inheritance looks like a parameter list in the class definition. Instead of including one base class insdie the parenthesis, we include two(or more) separated by a comma.

```
>>>e = EmailableContact("Test user ", "testuser@example.net")
>>>e.send_mail("hello, test email here")
Sending mail to testuser@example.net
```
- Multiple inheritance works all right when mixing methods from different classes, but it gets very messy when we have to work with calling methods on the superclass. Because there are multiple superclasses. How do we know which one to call? How do we know what order to call them in ?

### The Diamond Problem

- If we have two parent __init__ methods that both need to be initialized, and they need to initialized with different arguments. How do we do that? We can start with a naive approach:

```python
class Addressholder:
	def __init__(self, street, city, state, code):
		self.street = street
		self.city = city
		self.state = state
		self.code = code
	
class Friend(Contact, Addressholder):
	def __init__(self, name, email, phone, street, city, state, code):
		Contact.__init__(self, name, email)
		AddressHolder.__init__(self, street, city, state, code)
		self.phone = phone
```
In this example we directly call the __init__ function on each of the superclasses and explicitly pass the self argument. This example technically works;we can access the different varaibles directly on the class. But there are few problems.

1) There is a possibilty for a superclass to go uninitialized if we neglect to explicilty call the initializer .

2) Possibility of superclass being called multiple times, because of the organization of the class hierarchy. Inheritance diagram below.

<img src="mul_inher.JPG">

The __init__ method from the Friend class first calls __init__ on Contact which implicitly initializes the object superclass( all classes derive from obejct). Friend then calls __init__ on AddressHolder, which implicitly initializes the object superclass again. The parent class has been setup twice. Imagine trying to connect to a database twice for every request! The base class should only be called once.

- Technically the order in which methods can be called can be adapted on the fly by modifying the __mro__ (Method resolution Order) attribute of the class.

Let's look at a second example that illustrates this problem more clearly. Here er have a base class that has a method named call_me. Two subclasses override that method, and then another subclass extends both of these using multiple inheritance. This is called diamond inheritance because of the diamond shape of the class diagram:

<img src="diamond_problem.JPG">

Diamonds are what makes multiple inheritance tricky. Technically, all multiple inheritance in Python3 is diamond inheritance, because all classes inherit from object.

```python
# Diamond problem

class BaseClass:
	num_base_calls = 0
	def call_me(self):
		print("Calling method on Base class")
		self.num_base_calls += 1
		
class LeftSubclass(BaseClass):
	num_left_calls = 0
	def call_me(self):
		BaseClass.call_me(self)
		print('Calling method on LeftSubclass')
		self.num_left_calls += 1
		
class RightSubclass(BaseClass):
	num_right_calls = 0
	def call_me(self):
		BaseClass.call_me(self)
		print('Calling method on RightSubclass')
		self.num_right_calls += 1
		
class Subclass(LeftSubclass, RightSubclass):
	num_sub_calls = 0
	def call_me(self):
		LeftSubclass.call_me(self)
		RightSubclass.call_me(self)
		print('Calling method on subclass')
		self.num_sub_calls += 1
```

```
>>> s = Subclass()
>>> s.call_me()
Calling method on Base Class
Calling method on Left Subclass
Calling method on Base Class
Calling method on Right Subclass
Calling method on Subclass
>>> print(s.num_sub_calls, s.num_left_calls, s.num_right_calls,
s.num_base_calls)
1 1 1 2
```
The base class's call_me method has been called twice.

- The thing to keep in mind with multiple inheritance is that we only want to call the "next" method in the class hierarchy, not the "parent" method. In fact, that next method may not be on a parent or ancestor of the current class.
- The "super" keyword comes to our rescue once again. Indeed, super was originally developed to make complicated forms of multiple inheritance possible. Here is the same code written using super:

```python
class BaseClass:
	num_base_calls = 0
	def call_me(self):
		print("calling method on Base Class")
		self.num_base_calls += 1
		
class LeftSubclass(BaseClass):
	num_left_calls = 0
	def call_me(self):
		super().call_me()
		print("Calling method on Left Subclass")
		self.num_left_calls += 1
		
class RightSubclass(BaseClass):
	num_right_calls = 0
	def call_me(self):
		super().call_me()
		print('Calling method on Right Subclass")
		self.num_right_calls += 1
		
class Subclass(LeftSubclass, RightSubclass):
	num_sub_calls = 0
	def call_me(self):
		super().call_me()
		print("Calling method on Subclass")
		self.num_sub_calls += 1
```



```
>>> s = Subclass()
>>> s.call_me()
Calling method on Base Class
Calling method on Right Subclass
Calling method on Left Subclass
Calling method on Subclass
>>> print(s.num_sub_calls, s.num_left_calls, s.num_right_calls,
s.num_base_calls)
1 1 1 1
```

- Base method is only called once. First call_me of Subclass calls super().call_me(), which happens to refer to LeftSubclass.call_me(). LeftSubclass.call_me() then calls super().call_me(), but in this case, super() is referring to RightSubclass.call_me()
- The super call is not calling the method on the superclass of LeftSubclass(which is Baseclass), it is calling the RightSubclass, even though it is not a parent of LeftSubclass! This is the next method, not the parent method. RightSubclass then calls BaseClass and the super calls have ensured each method in the class hierarchy is executed once.



- Acknowledgement
Python 3 Object Oriented Programming by Dusty Phillips
