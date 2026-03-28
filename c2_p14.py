"""
A = amount after interest
p = principal deposited
r = annual interest rate
n = number of times interest compounded
t = number of years holding investment

user input
Amount deposited = p
interest rate paid by account = r
number of times interest compounded = n ex, quarterly = 4, monthly = 12
number of years account left in interest = t

Once data is input, program calcs and displays amount of money that will be in account after
specified number of years

"""


"""

print(5*5) # multiplication
print(5**2) # power
print(5 / 5) # division
print(5 // 4) # floor integer division
print(5 % 3) # modulous

"""

p = float(input("How much are you depositing?"))
r = float(input("What is your annual interest rate? (Enter as decimal)"))
n = float(input("How many times a year does the interest compound?"))
t = float(input("How many years are you holding the interest?"))

print(f"${p*(1 + r/n)**(t*n):,.2f}")