import functools

def broken_decorator(func):
    """A decorator that loses metadata."""
    def wrapper(*args, **kwargs):
        print("Executing broken_decorator...")
        return func(*args, **kwargs)
    return wrapper

def fixed_decorator(func):
    """A decorator that preserves metadata using functools.wraps."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Executing fixed_decorator...")
        return func(*args, **kwargs)
    return wrapper

@broken_decorator
def say_hi():
    """This function says hi."""
    print("Hi!")

@fixed_decorator
def say_bye():
    """This function says bye."""
    print("Bye!")

if __name__ == "__main__":
    print(f"--- Testing broken_decorator ---")
    print(f"Function Name: {say_hi.__name__}")
    print(f"Docstring: {say_hi.__doc__}")
    say_hi()

    print(f"\n--- Testing fixed_decorator ---")
    print(f"Function Name: {say_bye.__name__}")
    print(f"Docstring: {say_bye.__doc__}")
    say_bye()
    
    print("\nDeep Dive: functools.wraps copies __name__, __doc__, and other metadata from the original function to the wrapper.")
