"""
Day 8.1: The Linear Scan (O(N))

Goal: Create a list of 10 million numbers. Check if -1 is in the list.
Deep Dive: Python performs a Linear Search. It compares index 0, then 1...
until it hits the end. O(N).
"""
import time

def run_task():
    N = 10_000_000
    print(f"--- 8.1 Linear Scan (N={N}) ---")
    
    print("1. Generatng list...")
    data = list(range(N))
    
    target = -1 # A number that definitely isn't there (worst case)
    
    print("2. Starting scan for -1...")
    start_time = time.time()
    
    found = target in data
    
    end_time = time.time()
    
    print(f"Found: {found}")
    print(f"Time taken: {end_time - start_time:.5f} seconds")
    print("Note: If N doubles, this time will roughly double.\n")

if __name__ == "__main__":
    run_task()
