"""
Day 9.5: The Next Protocol

Goal: Manually call next(gen) until it crashes. 
Deep Dive: When a generator runs out of items, it raises a StopIteration exception. 
for loops catch this exception silently to stop looping.
"""

def countdown(n: int):
    while n > 0:
        yield n
        n -= 1

def run_task():
    print("--- 9.5 Next Protocol ---")
    c = countdown(3)
    
    print(f"Manual next: {next(c)}")
    print(f"Manual next: {next(c)}")
    print(f"Manual next: {next(c)}")
    
    try:
        print("Attempting one more next...")
        next(c)
    except StopIteration:
        print("Caught StopIteration! The generator has no more items.\n")

if __name__ == "__main__":
    run_task()
