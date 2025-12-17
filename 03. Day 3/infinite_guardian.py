\"\"\"Micro-Challenge: Infinite Guardian
Loop until user types 'stop'.
\"\"\"
while True:
    password = input("Enter password (type 'stop' to exit): ")
    if password == "stop":
        print("Exiting...")
        break
    print("Password recorded (not checked)")
