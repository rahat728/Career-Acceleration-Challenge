"""
Day 9.9: The Send Method

Goal: Use gen.send(value) to inject data into a running generator. 
Deep Dive: Generators can be two-way streets. val = yield pauses and waits to 
receive data from the outside world. This is the basis for Coroutines (AsyncIO).
"""

def talkative_gen():
    print("  Generator: Hello! I'm ready to receive.")
    msg = yield "I am waiting..."
    print(f"  Generator: I received '{msg}'")
    msg2 = yield f"You said {msg}. Anything else?"
    print(f"  Generator: And now I received '{msg2}'")

def run_task():
    print("--- 9.9 Send Method ---")
    g = talkative_gen()
    
    # Must "prime" the generator first
    initial_status = next(g)
    print(f"Main: Generator status: {initial_status}")
    
    # Now send data
    resp1 = g.send("Hello Generator!")
    print(f"Main: Generator response: {resp1}")
    
    try:
        g.send("Goodbye!")
    except StopIteration:
        print("Main: Generator finished.")
    print()

if __name__ == "__main__":
    run_task()
