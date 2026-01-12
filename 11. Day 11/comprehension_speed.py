# Goal: Compare map(lambda...) vs [x... for x...].
# Deep Dive: List Comprehensions are generally faster than map + lambda because they avoid the overhead of calling a Python function frame for every single item.

import timeit

def map_lambda():
    return list(map(lambda x: x * 2, range(1000)))

def list_comp():
    return [x * 2 for x in range(1000)]

if __name__ == "__main__":
    map_time = timeit.timeit(map_lambda, number=10000)
    comp_time = timeit.timeit(list_comp, number=10000)
    
    print(f"Map + Lambda time: {map_time:.4f}s")
    print(f"List Comprehension time: {comp_time:.4f}s")
    print(f"Difference: {abs(map_time - comp_time):.4f}s")
    
    if comp_time < map_time:
        print("List comprehension was faster!")
    else:
        print("Map + Lambda was faster (unlikely for this case).")
