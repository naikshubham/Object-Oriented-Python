# Original from_str method for reference:
#     @classmethod
#     def from_str(cls, datestr):
#         year, month, day = map(int, datestr.split("-"))
#         return cls(year, month, day)
  
# Define an EvenBetterDate class and customize from_str

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


class EvenBetterDate(BetterDate):
    @classmethod
    def from_str(cls, datestr, format="YYYY-MM-DD"):
        if format == "YYYY-MM-DD":
            return BetterDate.from_str(datestr)
        elif format == "DD-MM-YYYY":
            day, month, year = map(int, datestr.split("-"))
            return cls(year, month, day)

# This code should run with no errors
ebd_str = EvenBetterDate.from_str('02-12-2019', format='DD-MM-YYYY')
print(ebd_str.year)
ebd_dt = EvenBetterDate.from_datetime(datetime.today())
print(ebd_dt.year)