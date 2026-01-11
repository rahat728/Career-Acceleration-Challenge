import time

def timer(func):
    """
    A decorator that prints execution time of the decorated function.
    """
    def inner(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"--- [Timer] {func.__name__} took {execution_time:.4f} seconds ---")
        return result
    return inner

@timer
def heavy_computation():
    print("Starting heavy computation...")
    time.sleep(1.5) # Simulate a delay
    print("Computation complete.")

@timer
def fast_function():
    print("Running fast function...")

if __name__ == "__main__":
    heavy_computation()
    fast_function()
    print("\nDeep Dive: This is AOP (Aspect Oriented Programming). We inject timing logic without modifying the function code.")
