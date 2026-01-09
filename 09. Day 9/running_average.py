"""
Day 9.10: State Retention

Goal: Write a generator that calculates a "Running Average". 
Deep Dive: The generator remembers the total and count variables between yields. 
This eliminates the need for global variables or class attributes.
"""

def running_average():
    total = 0.0
    count = 0
    average = None
    
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count

def run_task():
    print("--- 9.10 State Retention (Running Average) ---")
    avg_gen = running_average()
    
    # Prime it
    next(avg_gen)
    
    data = [10, 20, 30, 40, 50]
    print(f"Feeding data: {data}")
    
    for val in data:
        current_avg = avg_gen.send(val)
        print(f"  Added {val}, Current Average: {current_avg}")
    
    print("\nNote: The 'total' and 'count' were kept inside the generator's local scope.\n")

if __name__ == "__main__":
    run_task()
