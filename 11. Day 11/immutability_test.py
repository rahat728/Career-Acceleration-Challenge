# Goal: Try to modify a tuple inside a map function.
# Deep Dive: Functional programming relies on **Immutability**. Functions should not have side effects. They should receive input and return new output.

def attempt_mutation(item):
    try:
        # Tuples are immutable, this should fail
        item[0] = item[0].upper()
    except TypeError as e:
        print(f"Mutation failed as expected: {e}")
    return (item[0].upper(), item[1])

data = [("apple", 1), ("banana", 2)]

if __name__ == "__main__":
    print(f"Original data: {data}")
    
    # map creates a NEW list (as an iterator), doesn't touch the original
    new_data = list(map(attempt_mutation, data))
    
    print(f"New data: {new_data}")
    print(f"Original data (unchanged): {data}")
