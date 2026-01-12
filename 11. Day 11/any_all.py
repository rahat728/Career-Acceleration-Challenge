# Goal: Check if any number in a list is negative. Check if all are positive.
# Deep Dive: These are short-circuiting operators. any() stops at the first True. all() stops at the first False. This is O(1) in the best case.

numbers = [1, 2, 3, -4, 5, 6]

has_negative = any(x < 0 for x in numbers)
all_positive = all(x > 0 for x in numbers)

if __name__ == "__main__":
    print(f"Numbers: {numbers}")
    print(f"Has negative? {has_negative}")
    print(f"All positive? {all_positive}")
    
    # Demonstration of short-circuiting
    def check(x):
        print(f"Checking {x}")
        return x > 0

    print("\nShort-circuit demo with all():")
    print(f"Result: {all(check(x) for x in [1, -2, 3])}") # Should stop at -2
