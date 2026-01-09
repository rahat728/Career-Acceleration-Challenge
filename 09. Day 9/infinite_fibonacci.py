"""
Day 9.3: The Infinite Sequence

Goal: Write a while True generator that produces Fibonacci numbers forever.
Deep Dive: This is impossible with a standard list (RAM would fill up). 
Generators allow Infinite Data Streams because they process one item at a time (Lazy Evaluation).
"""
import time

def fibonacci_gen():
    """Generator for infinite Fibonacci sequence."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def run_task():
    print("--- 9.3 Infinite Sequence (Fibonacci) ---")
    fib = fibonacci_gen()
    
    print("First 15 Fibonacci numbers:")
    for i in range(15):
        print(next(fib), end=" ")
    print("\n\nGenerators can theoretically run forever without memory issues.")
    print("Example: Processing real-time sensor data or logs.\n")

if __name__ == "__main__":
    run_task()
