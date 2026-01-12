# Goal: Square a list of numbers using map().
# Deep Dive: map(func, list) pushes the loop into C-speed. It returns an iterator (lazy).

numbers = [1, 2, 3, 4, 5]
squares = map(lambda x: x**2, numbers)

if __name__ == "__main__":
    print(f"Original numbers: {numbers}")
    print(f"Squares (as iterator): {squares}")
    
    # Triggering execution with list()
    squares_list = list(squares)
    print(f"Squares (as list): {squares_list}")
