
# Object-Oriented Python

Class lets us bundle behaviour and state together in an object.
- Behavior : function
- State    : variables

To use a class, we can create an object from it. This is known as Object instantiation.

- When we create objects from a class, each object shares the class's coded methods, but maintains its own copy of varaibles.
- The first argument to every method is always "self" and its value is supplied by the interpreter

### Constructor
- Construction `__init__()` method is called every time an object is created.

### Class-level data
- Data shared among all instances of a class. "Global variable" within the class.`MIN_SALARY` is shared among all instances.
- Dont use `self` to define class attribute and use `ClassName.ATTR_NAME` to access the class attribute value.

```python
class Employee:
	# define a class attribute
	MIN_SALARY = 30000 #<---no self
	def __init__(self, name, salary):
		self.name = name
		# use class name to access class attribute
		if salary >= Employee.MIN_SALARY:
			self.salary = salary
		else:
			self.salary = Employee.MIN_SALARY

	@classmethod
	def from_file(cls, filename):
		with open(filename, 'r') as f:
			name = f.readline()
		return cls(name)

emp = Employee.from_file("employee_data.txt")
```

### Class methods
- Methods are already shared : same code for every instance. Class methods cant use instance-level data.

```python
class MyClass:

	@classmethod                #<--use decorator to declare a class method
	def my_method(cls, args..): #<--cls argument refers to the class
		# execute
		# can't use any instance attributes
```

- To call a class method we use `MyClass.my_method(args...)` syntax rather then obj.my_method syntax.

#### Alternative constructors
- why would we ever need class methods at all? The main use case is `Alternative constructors`. A class can only have one __init__ method, but there might be multiple ways to initialize an object.
- For e.g, we might want to create a Employee object from data stored in a file, we can't use a method because that would require an instance and there isn't one yet.
- Here we introduce a class method `from_file` (refer above example) that accepts a filename, reads the firstname from the file that reads the name from file, name of the employee and returns an object instance. In the return statement `cls` is used. `cls` refers to the class. **This line will call the __init__ constructor just like calling Employee with the parenthesis**.
- Then we call the method `from_file` by using Class.method syntax which will create a Employee object without explicitly calling the constructor.

### Inheritance
- Code reuse. New class functionality = old class functionality + extra

```python
# implementening class inheritance
class MyChild(MyParent):
	# execute
```

### Customizing constructors

```python
class BankAccount:
	def __init__(self, balance):
		self.balance = balance

	def withdraw(self, amount):
		self.balance -= amount

class SavingsAccount(BankAccount):
	# constructor specifically for SavingsAccount with an additional parameter
	def __init__(self, balance, interest_rate):
		# call the parent constructor using ClassName.__init__()
		BankAccount.__init__(self, balance) # <--- self is a SavingsAccount but also a BankAccount
		# add more functionality
		self.interest_rate = interest_rate
		# construct the object using the new constructor
		acct = SavingsAccount(1000, 0.03)
		acct.interest_rate
```

- Can run constructor of the parent class first by `Parent.__init__(self, args...)`. We used `BankAccount.__init__(self, balance)` to tell Python to call the constructor from Parent class.
- `self` in this case is an savings account, that's the class we are in. In Python the instances of the subclass are also instances of parent class.

### Adding functionality
- Add methods as usual. Can use the data from both the parent and the child class.

```python
class SavingsAccount(BankAccount):
	def __init__(self, balance, interest_rate):
		BankAccount.__init__(self, balance)
		self.interest_rate = interest_rate

	# new functionality
	def compute_interest(self, n_periods=1):
		return self.balance * ((1 + self.interest_rate) ** n_periods - 1)
```

### Customizing functionality

```python
class CheckingAccount(BankAccount):
	def __init__(self, balance, limit):
		BankAccount.__init__(self, content)
		self.limit = limit

	def deposit(self, amount):
		self.balance += amount

	# new argument to withdraw fee
	def withdraw(self, amount, fee=0):
		# compare the fee to limit and then call parent withdraw method
		if fee <= self.limit:
			BankAccount.withdraw(self, amount - fee)
		else:
			BankAccount.withdraw(self, amount - limit)

```








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
