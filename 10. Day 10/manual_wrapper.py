def wrapper(func):
    """
    A manual wrapper function that demystifies the @ syntax.
    It takes a function and returns a new function that adds behavior.
    """
    def inner():
        print("--- Before the function call ---")
        func()
        print("--- After the function call ---")
    
    return inner

def say_hello():
    print("Hello, Intelligence Academy!")

# Manual Application
# This is exactly what @wrapper does under the hood
say_hello = wrapper(say_hello)

if __name__ == "__main__":
    print("Executing manually wrapped function:")
    say_hello()
