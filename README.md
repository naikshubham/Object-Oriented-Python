

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

   
