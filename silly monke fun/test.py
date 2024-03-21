def calculate_circle_properties(diameter):
    radius = diameter / 2
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

def main():
    diameter = float(input("Enter the diameter of the circle: "))
    area, circumference = calculate_circle_properties(diameter)
    print("Area of the circle:", area)
    print("Circumference of the circle:", circumference)

if __name__ == "__main__":
    main()
