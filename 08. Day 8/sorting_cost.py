"""
Day 8.8: The Sorting Cost

Goal: Sort a random list.
Deep Dive: Timsort is O(N log N).
"""
import time
import random

def run_task():
    N = 1_000_000
    print(f"--- 8.8 Sorting Cost (N={N}) ---")
    
    data = [random.randint(0, N) for _ in range(N)]
    
    print("Sorting...")
    start = time.time()
    data.sort()
    end = time.time()
    
    print(f"Time taken: {end - start:.5f} seconds")
    print("Conclusion: Fast, but don't do it inside a loop.\n")

if __name__ == "__main__":
    run_task()
