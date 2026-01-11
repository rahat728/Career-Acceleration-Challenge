def bold(func):
    """Adds <b> tags around the result."""
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic(func):
    """Adds <i> tags around the result."""
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}<i>"
    return wrapper

@bold
@italic
def greet(name):
    return f"Hello, {name}"

if __name__ == "__main__":
    print(f"Greet Result: {greet('Rahat')}")
    print("\nDeep Dive: Decorators stack from bottom to top (Inner to Outer).")
    print("@bold @italic greet() becomes bold(italic(greet())). Order matters!")
