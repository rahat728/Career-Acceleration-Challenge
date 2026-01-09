"""
Day 9.4: The One-Time Trap

Goal: Create a generator g. Loop through it once. Try to loop through it again.
Deep Dive: Generators are Exhaustible. Once iterated, the "cursor" is at the end.
You cannot rewind a generator; you must re-instantiate it.
"""

def simple_gen():
    yield "Python"
    yield "is"
    yield "Awesome"

def run_task():
    print("--- 9.4 One-Time Trap ---")
    g = simple_gen()
    
    print("First pass:")
    for item in g:
        print(f"  {item}")
        
    print("Second pass (expecting nothing):")
    for item in g:
        print(f"  {item}")
    
    print("Note: The second loop produced nothing because the generator is exhausted.")
    
    # To use again, must re-instantiate
    print("Re-instantiating for third pass:")
    g = simple_gen()
    for item in g:
        print(f"  {item}")
    print()

if __name__ == "__main__":
    run_task()
