\"\"\"Micro-Challenge: Reference Trap
Demonstrate list aliasing and fix with copy().
\"\"\"
a = [1, 2, 3]
b = a  # Aliasing
b[0] = 99
print("After mutation via b:", a)  # Changed!

# Fixed version
a = [1, 2, 3]
b = a.copy()
b[0] = 999
print("After copy and mutation:", a)  # Unchanged
