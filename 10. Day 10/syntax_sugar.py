def simple_decorator(func):
    """
    A simple decorator that uses syntax sugar.
    """
    def inner():
        print(">>> Decorator logic running...")
        func()
        print(">>> Decorator logic complete.")
    return inner

@simple_decorator
def shout():
    print("I AM SHOUTING!")

if __name__ == "__main__":
    print("Executing decorated function (@ syntax):")
    shout()
