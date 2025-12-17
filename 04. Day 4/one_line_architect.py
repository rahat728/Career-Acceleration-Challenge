\"\"\"Micro-Challenge: One-Line Architect
List comprehension: squares of even numbers 1-10.
\"\"\"
numbers = range(1, 11)
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(even_squares)  # [4, 16, 36, 64, 100]
