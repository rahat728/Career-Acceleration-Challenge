"""
Day 9.7: The Large File Reader

Goal: Write a generator to read a "fake" 100GB file line-by-line. 
Deep Dive: Using yield line allows you to process datasets larger than your 
machine's physical RAM. This is the standard for Big Data processing in Python.
"""
import random

def simulate_massive_file(lines=10):
    """Simulates reading a huge file by yielding lines one by one."""
    for i in range(1, lines + 1):
        # In a real scenario, this would be: for line in open('huge_file.csv'): yield line
        yield f"LOG_ENTRY_{i:04d}: User_{random.randint(100, 999)} performed action {random.choice(['LOGIN', 'LOGOUT', 'PURCHASE'])}"

def run_task():
    print("--- 9.7 Large File Reader ---")
    print("Reading '100GB' file line-by-line...")
    
    reader = simulate_massive_file(5)  # Let's just read 5 for the demo
    for line in reader:
        print(f"  Processing line: {line.strip()}")
        
    print("\nDeep Dive: Real code would use 'with open(path) as f: for line in f: yield line'")
    print("This ensures only one line is in memory at a time.\n")

if __name__ == "__main__":
    run_task()
