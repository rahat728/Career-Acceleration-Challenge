"""
Day 8.2: The Hash Lookup (O(1))

Goal: Convert list to set. Check for -1 again.
Deep Dive: Python runs hash(-1), jumps directly to memory slot. 
It never scans the other items. O(1).
"""
import time

def run_task():
    N = 10_000_000
    print(f"--- 8.2 Hash Lookup (N={N}) ---")
    
    print("1. Generating list and converting to SET...")
    # Conversion takes O(N), but lookups afterwards are O(1)
    data_set = set(range(N))
    
    target = -1
    
    print("2. Starting lookup for -1...")
    start_time = time.time()
    
    found = target in data_set
    
    end_time = time.time()
    
    print(f"Found: {found}")
    print(f"Time taken: {end_time - start_time:.10f} seconds")
    print("Note: This is nearly instant, regardless of N.\n")

if __name__ == "__main__":
    run_task()
