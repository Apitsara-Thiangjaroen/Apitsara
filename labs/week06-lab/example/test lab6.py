def calculate_rectangle_area(length, width):
    """Calculates and displays rectangle area"""
    area = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area = {length} × {width} = {area}")
    print()

print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)

def calculate_triangle_area(height, base):
    """Calculates and displays triangle area"""
    area = 0.5 * height * base
    print(f"Triangle with height {height} and base {base}")
    print(f"Area = {height} × {base} = {area}")
    print()

print("Calculating_triangle_areas:")
calculate_triangle_area(5, 3)
calculate_triangle_area(10, 7)

# จากตัวอย่าง ให้สร้าง function สำหรับพื้นที่วงกลม

def calculate_circle_area(radius):
    """Calculates and displays circle area"""
    area = 3.14 * radius * radius
    print(f"Circle with radius {radius}")
    print(f"Area = pi × {radius}² = {area}")
    print()

print("Calculating circle areas:")
calculate_circle_area(5)
calculate_circle_area(10)




