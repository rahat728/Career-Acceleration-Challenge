\"\"\"Micro-Challenge: Type Auditor
Show type before and after casting input to float.
\"\"\"
raw = input("Enter a number: ")
print(f"Raw input type: {type(raw)}")

try:
    number = float(raw)
    print(f"After casting: {type(number)}")
except ValueError:
    print("Invalid input for float conversion")
