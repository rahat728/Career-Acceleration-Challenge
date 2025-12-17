\"\"\"Micro-Challenge: Floating Point Trap
Demonstrate 0.1 + 0.2 != 0.3 and proper comparison.
\"\"\"
print("Direct comparison:", 0.1 + 0.2 == 0.3)  # False

# Proper way with tolerance
tolerance = 1e-9
print("With tolerance:", abs((0.1 + 0.2) - 0.3) < tolerance)  # True
