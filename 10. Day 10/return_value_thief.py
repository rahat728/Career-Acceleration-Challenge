def thief_decorator(func):
    """
    A decorator that 'steals' the return value because it doesn't return anything.
    """
    def inner(*args, **kwargs):
        print(f"I am calling {func.__name__} but I won't give you the result!")
        func(*args, **kwargs)
        # Missing return statement here!
    return inner

def honest_decorator(func):
    """
    A decorator that correctly captures and returns the original result.
    """
    def inner(*args, **kwargs):
        print(f"I am calling {func.__name__} and I WILL return the result.")
        result = func(*args, **kwargs)
        return result
    return inner

@thief_decorator
def multiply_stolen(a, b):
    return a * b

@honest_decorator
def multiply_honest(a, b):
    return a * b

if __name__ == "__main__":
    print(f"Testing multiply_stolen(5, 5):")
    res1 = multiply_stolen(5, 5)
    print(f"Result: {res1}") # Should be None
    
    print(f"\nTesting multiply_honest(5, 5):")
    res2 = multiply_honest(5, 5)
    print(f"Result: {res2}") # Should be 25
