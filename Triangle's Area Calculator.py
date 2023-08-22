def calculate_rectangle_properties(length, width):
    """
    Calculate the area and perimeter of a rectangle.
    
    Args:
        length (float): Length of the rectangle.
        width (float): Width of the rectangle.
    
    Returns:
        tuple: A tuple containing the area and perimeter.
    """
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

def main():
    print("Welcome to the Rectangle Properties Calculator!")

    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    area, perimeter = calculate_rectangle_properties(length, width)

    print(f"\nRectangle Properties:")
    print(f"Length: {length}")
    print(f"Width: {width}")
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")

if __name__ == "__main__":
    main()
