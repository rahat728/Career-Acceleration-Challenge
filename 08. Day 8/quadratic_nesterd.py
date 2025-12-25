"""
Day 8.7: The Quadratic Nested Loop (O(N^2))

Goal: Find duplicates between two lists using nested loops.
Deep Dive: 10k x 10k = 100M operations.
"""
import time

def run_task():
    N = 5_000 # Kept small because N^2 explodes fast
    print(f"--- 8.7 Nested Loops (N={N}) ---")
    
    list_a = list(range(N))
    list_b = list(range(N))
    
    print("Running nested loop check...")
    start = time.time()
    
    count = 0
    # O(N^2) Logic
    for x in list_a:
        for y in list_b:
            if x == y:
                count += 1
                
    end = time.time()
    print(f"Matches found: {count}")
    print(f"Time taken: {end - start:.5f} seconds")
    
    # Optimization demonstration
    print("\n--- Optimization (Set Intersection) ---")
    start_opt = time.time()
    set_a = set(list_a)
    set_b = set(list_b)
    count_opt = len(set_a.intersection(set_b))
    print(f"Set time: {time.time() - start_opt:.5f} seconds (O(N))")
    print("Conclusion: Sets eliminate nested loops.\n")

if __name__ == "__main__":
    run_task()
