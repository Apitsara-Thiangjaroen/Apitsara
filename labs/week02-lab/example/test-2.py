print("4. BMI Calculator:")
print("   - Ask for weight (kg) and height (m)")
print("   - Calculate: BMI = weight / (height ** 2)")
print()

#input
weight = float(input("Enter your weight (kg):"))
height = float(input("Enter your height (m):"))

#process
bmi = weight / (height **2)

#output
print(f"Your BMI is : {bmi:.2f}")
