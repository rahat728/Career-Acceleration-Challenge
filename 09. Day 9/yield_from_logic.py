"""
Day 9.8: Yield From

Goal: Write a generator that yields values from two different sub-generators using yield from. 
Deep Dive: yield from delegates the generator operation to another sub-generator. 
It flattens nested structures efficiently without manual loops.
"""

def sub_gen_a():
    yield "Alpha"
    yield "Beta"

def sub_gen_b():
    yield "Gamma"
    yield "Delta"

def master_gen():
    print("Starting Sub-Generator A...")
    yield from sub_gen_a()
    print("Starting Sub-Generator B...")
    yield from sub_gen_b()
    yield "Omega"

def run_task():
    print("--- 9.8 Yield From ---")
    for val in master_gen():
        print(f"  Value: {val}")
    print("yield from makes it easy to compose complex generators from smaller ones.\n")

if __name__ == "__main__":
    run_task()
