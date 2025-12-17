\"\"\"Micro-Challenge: Accumulator Pattern
Sum numbers from 1 to N using loop (no formula).
\"\"\"
n = int(input("Enter N: "))
total = 0
for i in range(1, n + 1):
    total += i
print(f"Sum from 1 to {n}: {total}")
