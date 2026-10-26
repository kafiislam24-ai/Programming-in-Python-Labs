import math

def calculate_distance():
    print("Enter the coordinates for the first point (x1, y1):")
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    
    print("\nEnter the coordinates for the second point (x2, y2):")
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    
    
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    print(f"\nThe distance between the points ({x1}, {y1}) and ({x2}, {y2}) is: {distance:.2f}")

calculate_distance()