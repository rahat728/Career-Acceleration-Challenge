"""
Day 9.6: The Pipeline (Chaining)

Goal: Create two generators: one squares numbers, the other filters evens. 
Chain them: filter(square(nums)). 
Deep Dive: This creates a Data Pipeline. Data flows from source -> square -> filter 
one item at a time. No intermediate lists are created in RAM.
"""

def square_gen(nums):
    for n in nums:
        yield n * n

def even_filter_gen(nums):
    for n in nums:
        if n % 2 == 0:
            yield n

def run_task():
    print("--- 9.6 Pipeline (Chaining) ---")
    raw_data = range(1, 11)
    
    # Chaining generators
    squared = square_gen(raw_data)
    evens_only = even_filter_gen(squared)
    
    print("Original: 1 to 10")
    print("Pipeline Output (Squared and Even Only):")
    for result in evens_only:
        print(f"  Processed: {result}")
        
    print("Note: Each number was processed individually through the pipeline.\n")

if __name__ == "__main__":
    run_task()
