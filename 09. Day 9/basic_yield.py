"""
Day 9.1: The Basic Yield

Goal: Write a function gen() that yields 1, then 2, then 3. Loop through it.
Deep Dive: Unlike return, yield pauses the function and saves the Stack Frame 
(local variables) in RAM. The function is "frozen" until you call it again.
"""

def gen():
    """A simple generator that yields three numbers."""
    print("  Starting generator...")
    yield 1
    print("  Resuming for second yield...")
    yield 2
    print("  Resuming for third yield...")
    yield 3
    print("  Generator exhausted.")

def run_task():
    print("--- 9.1 Basic Yield ---")
    g = gen()
    print(f"Generator object created: {g}")
    
    for val in g:
        print(f"Received: {val}")
    print("Loop finished.\n")

if __name__ == "__main__":
    run_task()
