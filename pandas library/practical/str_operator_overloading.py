class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Implement the __str__() method
    def __str__(self):
        return f"Point({self.x}, {self.y})"

# Create an instance of Point
p1 = Point(3, 7)

# Print the Point object
print(p1)