"""
Day 8.10: The Slice Copy

Goal: Slice a massive list.
Deep Dive: Slicing allocates NEW memory and copies references.
It is O(k) where k is the slice size.
"""
import time

def run_task():
    N = 10_000_000
    print(f"--- 8.10 Slice Copy (Source N={N}) ---")
    
    data = list(range(N))
    
    # Small Slice
    k_small = 100
    start = time.time()
    _ = data[:k_small]
    print(f"Slice 100 items:     {time.time() - start:.8f} seconds")
    
    # Huge Slice
    k_huge = 9_000_000
    start = time.time()
    _ = data[:k_huge]
    print(f"Slice 9M items:      {time.time() - start:.5f} seconds")
    print("Conclusion: Slicing isn't free. It copies data.\n")

if __name__ == "__main__":
    run_task()
