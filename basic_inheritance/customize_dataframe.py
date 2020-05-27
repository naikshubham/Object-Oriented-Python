# Customizing a DataFrame
# Any data has to come with a timestamp recording when the dataset was created, to make sure that outdated information is not being used.
# We would like to use pandas DataFrames for processing data, but we would need to customize the class to allow for the use of timestamps.

# We will implement a small LoggedDF class that inherits from a regular pandas DataFrame but has a created_at attribute storing the timestamp. 
# We will then augment the standard to_csv() method to always include a column storing the creation date.

# Tip: all DataFrame methods have many parameters, and it is not sustainable to copy all of them for each method we're customizing.
# The trick is to use variable-length arguments *args and **kwargsto catch all of them.

# Import pandas as pd
import pandas as pd

# Define LoggedDF inherited from pd.DataFame and add the constructor
class LoggedDF(pd.DataFrame):
  
  def __init__(self, *args, **kwargs):
    pd.DataFrame.__init__(self, *args, **kwargs)
    self.created_at = datetime.today()
    
  def to_csv(self, *args, **kwargs):
    # Copy self to a temporary DataFrame
    temp = self.copy()
    
    # Create a new column filled with self.created at
    temp["created_at"] = self.created_at
    
    # Call pd.DataFrame.to_csv on temp with *args and **kwargs
    pd.DataFrame.to_csv(temp, *args, **kwargs)
    
# Incredible work! Using *args and **kwargs allows you to not worry about keeping the signature of your customized method compatible.
# Notice how in the very last line, we called the parent method and passed an object to it that isn't self. 
# When we call parent methods in the class, they should accept some object as the first argument, and that object is usually self, but it doesn't have to be!