"""
Day 9.2: The Memory Profile

Goal: Compare sys.getsizeof() of a List Comprehension vs a Generator Expression for 1 million numbers.
Deep Dive: [x for x in range(1M)] consumes ~8MB RAM (stores all numbers). 
(x for x in range(1M)) consumes ~100 Bytes (stores only the logic).
"""
import sys

def run_task():
    print("--- 9.2 Memory Profile ---")
    N = 1_000_000
    
    # List Comprehension
    list_comp = [x for x in range(N)]
    list_size = sys.getsizeof(list_comp)
    
    # Generator Expression
    gen_exp = (x for x in range(N))
    gen_size = sys.getsizeof(gen_exp)
    
    print(f"List Comprehension (N={N}) size: {list_size:,} bytes")
    print(f"Generator Expression (N={N}) size: {gen_size:,} bytes")
    print(f"Generator is {list_size / gen_size:.2f}x more memory efficient in this case.\n")

if __name__ == "__main__":
    run_task()
