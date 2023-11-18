class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance(self):
        return (self.x, self.y, self.z)

# Create a variable containing a new instances
my_point = Point3D(x=1, y=2, z=3)
# Print the distance of the point
print(my_point.distance())

#QUESTION 2
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.width * self.length
    def perimeter(self):
        return 2 * (self.length + self.width)
my_rectangle = Rectangle(width=3, length=4)

#Compute both area and perimeter
area_result = my_rectangle.area()
perimeter_result = my_rectangle.perimeter()
print(f"Area: {area_result}")
print(f"Perimeter: {perimeter_result}")

#QUESTION 3
import math

class Circle:
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def is_inside(self, point_x, point_y):
        distance = math.sqrt((point_x - self.center_x)**2 + (point_y - self.center_y)**2)
        return distance <= self.radius

# Create an instance of Circle
my_circle = Circle(center_x=0, center_y=0, radius=5)

# Compute and print the area and perimeter
area_result = my_circle.area()
perimeter_result = my_circle.perimeter()

print(f"Area: {area_result}")
print(f"Perimeter: {perimeter_result}")

# Test if a point is inside the circle
point_x = 3
point_y = 4
if my_circle.is_inside(point_x, point_y):
    print(f"Point ({point_x}, {point_y}) is inside the circle.")
else:
    print(f"Point ({point_x}, {point_y}) is outside the circle.")

#QUESTION 4
class Bank:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        elif amount <= 0:
            print("Invalid withdrawal amount. Amount must be greater than 0.")
        else:
            print("Insufficient funds for withdrawal.")

# Create an instance of Bank with an initial balance of $100
my_bank_account = Bank(initial_balance=100)

# Deposit and withdraw operations
my_bank_account.deposit(50)
my_bank_account.withdraw(30)
my_bank_account.withdraw(150)  # Attempting to withdraw more than the balance
my_bank_account.deposit(-20)  # Attempting to deposit a negative amount


