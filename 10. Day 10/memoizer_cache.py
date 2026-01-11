def cache(func):
    """
    A decorator that caches the results of function calls.
    """
    history = {} # Storage for results
    
    def inner(n):
        if n in history:
            return history[n]
        
        result = func(n)
        history[n] = result
        return result
    
    return inner

@cache
def fibonacci(n):
    """A recursive implementation of Fibonacci."""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    import time
    
    print("Calculating Fibonacci(35) with @cache...")
    start = time.time()
    res = fibonacci(35)
    end = time.time()
    
    print(f"Result: {res}")
    print(f"Time taken: {end - start:.6f} seconds")
    print("\nDeep Dive: Without @cache, Fibonacci(35) would take significantly longer due to redundant calculations.")
