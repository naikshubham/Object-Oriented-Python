'''
Alternative constructors

Python allows us to define class methods as well, using the @classmethod decorator and a special first argument cls. The main use of class methods is defining methods that return an instance of the class, but aren't using the same code as __init__().

For example, we are developing a time series package and want to define our own class for working with dates, BetterDate. The attributes of the class will be year, month, and day. You want to have a constructor that creates BetterDate objects given the values for year, month, and day, but we also want to be able to create BetterDate objects from strings like 2020-04-30.

We might find the following functions useful:

    .split("-") method will split a string at"-" into an array, e.g. "2020-04-30".split("-") returns ["2020", "04", "30"],
    int() will convert a string into a number, e.g. int("2019") is 2019 .
'''
from datetime import datetime

class BetterDate:    
    # Constructor
    def __init__(self, year, month, day):
      # Recall that Python allows multiple variable assignments in one line
      self.year, self.month, self.day = year, month, day
    
    # Define a class method from_str
    @classmethod
    def from_str(cls, datestr):
        # Split the string at "-" and convert each part to integer
        parts = datestr.split("-")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        # Return the class instance
        return cls(year, month, day)
        
    # Define a class method from_datetime accepting a datetime object
    @classmethod
    def from_datetime(cls, datetime):
        return cls(datetime.year, datetime.month, datetime.day)

bd = BetterDate.from_str('2020-04-30')   
print(bd.year)
print(bd.month)
print(bd.day)


# You should be able to run the code below with no errors: 
today = datetime.today()     
bd = BetterDate.from_datetime(today)   
print(bd.year)


'''
There's another type of methods that are not bound to a class instance - static methods, defined with the decorator @staticmethod.
 They are mainly used for helper or utility functions that could as well live outside of the class, but make more sense when bundled into the class. 
'''