"""
Day 8.5: The String Builder

Goal: s += 'a' vs list join.
Deep Dive: Strings are Immutable. += creates a brand new string every time.
"""
import time

def run_task():
    N = 100_000
    print(f"--- 8.5 String Builder (N={N}) ---")

    # TEST 1: Bad Concatenation
    start = time.time()
    s = ""
    for _ in range(N):
        s += "a" # Allocates new memory, copies old string, adds 'a'
    print(f"String += loop: {time.time() - start:.5f} seconds")

    # TEST 2: Good (List Join)
    start = time.time()
    parts = []
    for _ in range(N):
        parts.append("a")
    final_s = "".join(parts)
    print(f"List .join():   {time.time() - start:.5f} seconds")
    print("Conclusion: join() is significantly faster for many strings.\n")

if __name__ == "__main__":
    run_task()
