# Goal: Remove all negative numbers from a list using filter().
# Deep Dive: filter(func, list) keeps items where func(item) returns Truthy.

numbers = [10, -5, 0, 8, -2, 4, -1]
positives = filter(lambda x: x >= 0, numbers)

if __name__ == "__main__":
    print(f"Original numbers: {numbers}")
    print(f"Positive numbers: {list(positives)}")
    
    # Demonstrating passing None to filter (filters out Falsy values: 0, "", None)
    mixed = [1, 0, 2, "", 3, None, "Hello"]
    truthy_only = filter(None, mixed)
    print(f"Truthy values only: {list(truthy_only)}")
