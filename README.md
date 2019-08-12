

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

1) There is a possibilty for a superclass to go uninitialized if we neglect to explicilty call the initializer 
	


   
