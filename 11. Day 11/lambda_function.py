# Goal: Write a function add(x, y) using lambda.
# Deep Dive: lambda creates a function object on the heap but assigns it no name.

add = lambda x, y: x + y

if __name__ == "__main__":
    result = add(5, 3)
    print(f"5 + 3 = {result}")
    print(f"Type of add: {type(add)}")
