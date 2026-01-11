def universal_wrapper(func):
    """
    A decorator that can handle any number of positional and keyword arguments.
    """
    def inner(*args, **kwargs):
        print(f"--- Calling function: {func.__name__} ---")
        print(f"--- Arguments: {args}, {kwargs} ---")
        func(*args, **kwargs)
        print(f"--- Finished calling: {func.__name__} ---")
    
    return inner

@universal_wrapper
def add(a, b):
    print(f"Calculation: {a} + {b} = {a + b}")

@universal_wrapper
def greet(name, message="Hi"):
    print(f"{message}, {name}!")

if __name__ == "__main__":
    print("Testing with two arguments:")
    add(10, 20)
    
    print("\nTesting with keyword arguments:")
    greet("Rahat", message="Welcome")
    
    print("\nTesting with positional arguments:")
    greet("Alice")
