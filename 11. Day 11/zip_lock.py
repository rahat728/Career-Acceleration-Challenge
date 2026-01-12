# Goal: Combine names=["A", "B"] and ages=[20, 30] into a dictionary.
# Deep Dive: dict(zip(names, ages)). zip creates an iterator of tuples. dict() consumes those tuples to build the hash map.

names = ["A", "B", "C"]
ages = [20, 30, 40]

# Combine using zip and convert to dict
user_data = dict(zip(names, ages))

if __name__ == "__main__":
    print(f"Names: {names}")
    print(f"Ages: {ages}")
    print(f"Zipped (interator): {zip(names, ages)}")
    print(f"Dictionary: {user_data}")
