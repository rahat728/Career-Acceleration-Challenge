# Goal: Calculate the product of a list (1*2*3*4) using functools.reduce.
# Deep Dive: Reduce collapses a list into a single value.

from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)

if __name__ == "__main__":
    print(f"Numbers: {numbers}")
    print(f"Product: {product}")
    
    # With initial value
    product_with_initial = reduce(lambda x, y: x * y, numbers, 10)
    print(f"Product with initial value 10: {product_with_initial}")
