# Create the Account class
class Account:
  """The Account class stores the details of each account and has methods to deposit, withdraw and calculate progress towards the savings goal"""
  def __init__(self, name, balance, goal):
    self.name = name
    self.balance = balance
    self.goal = goal
  
  # Deposit method adds money to balance
  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
      return True
    else:
      return False
  
  # Withdraw method subtracts money from balance
  def withdraw(self, amount):
    if amount > 0 and amount <= self.balance:
      self.balance -= amount
      return True
    else:
      return False
      
  # Get progress method calculates goal progress
  def get_progress(self):
    progress = (self.balance/self.goal) * 100
    return progress
  
  
# Create instances of the class
savings = Account("Savings", 0, 1000)
phone = Account("Phone", 0, 800)
holiday = Account("Holiday", 0, 7000)
 
# Print out some attributes
print(savings.name)
print(phone.balance)
print(holiday.goal)
#print(help(Account))

# Test the deposit method
savings.deposit(50)
print(savings.balance)
savings.withdraw(10)
print(savings.balance)
savings.withdraw(1200)
print(savings.balance)

print(savings.get_progress())
