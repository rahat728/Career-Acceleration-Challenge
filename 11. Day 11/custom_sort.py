# Goal: Sort ["100px", "20px", "3px"] numerically (so 3px comes first).
# Deep Dive: sorted(data, key=lambda x: int(x[:-2])). The key function transforms the item only for comparison.

data = ["100px", "20px", "3px"]

# Sorting numerically by stripping 'px' and converting to int
sorted_data = sorted(data, key=lambda x: int(x[:-2]))

if __name__ == "__main__":
    print(f"Original data: {data}")
    print(f"Lexicographical sort (default): {sorted(data)}")
    print(f"Numerical sort: {sorted_data}")
