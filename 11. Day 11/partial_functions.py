# Goal: Create a function power(base, exp). Use functools.partial to create a new function square(x) that locks exp=2.
# Deep Dive: Partials "freeze" arguments. This is useful when you need to pass a function to a callback (like in UI frameworks) that expects fewer arguments.

from functools import partial

def power(base, exp):
    return base ** exp

# Create a specialized function using partial
square = partial(power, exp=2)
cube = partial(power, exp=3)

if __name__ == "__main__":
    print(f"5 squared: {square(5)}")
    print(f"5 cubed: {cube(5)}")
    print(f"Function signature of square: {square}")
