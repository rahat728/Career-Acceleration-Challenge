"""
Day 8.6: The Length Trick

Goal: Call len() on a massive list.
Deep Dive: len() reads a cached integer 'ob_size' in C struct. It does not count.
"""
import time

def run_task():
    N = 50_000_000
    print(f"--- 8.6 Length Trick (N={N}) ---")
    
    print("Generating massive list...")
    data = list(range(N))
    
    print("Timing len()...")
    start = time.time()
    length = len(data)
    end = time.time()
    
    print(f"Length: {length}")
    print(f"Time: {end - start:.10f} seconds")
    print("Conclusion: Instant. Don't fear calling len().\n")

if __name__ == "__main__":
    run_task()
