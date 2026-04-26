# Day 2 - Simple Calculator

print("=== Simple Calculator ===")

# Get input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calculate
addition       = num1 + num2
subtraction    = num1 - num2
multiplication = num1 * num2
division       = num1 / num2

# Show results
print("Addition:      ", addition)
print("Subtraction:   ", subtraction)
print("Multiplication:", multiplication)
print("Division:      ", division)