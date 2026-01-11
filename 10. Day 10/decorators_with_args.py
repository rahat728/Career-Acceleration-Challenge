import functools

def repeat(times=3):
    """
    A decorator factory that creates a decorator based on given arguments.
    Level 1: The Factory (receives 'times')
    """
    def decorator(func):
        """Level 2: The Decorator (receives 'func')"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """Level 3: The Wrapper (receives 'args', 'kwargs')"""
            result = None
            print(f"--- Repeating {func.__name__} {times} times ---")
            for i in range(times):
                print(f"Execution {i+1}:")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=2)
def ping():
    print("Pong!")

@repeat(times=5)
def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    ping()
    print("-" * 30)
    greet("Intelligence Academy")
    
    print("\nDeep Dive: This requires Three Levels of Nested Functions:")
    print("1. The Factory (accepts 'times')")
    print("2. The Decorator (accepts 'func')")
    print("3. The Wrapper (accepts 'args')")
