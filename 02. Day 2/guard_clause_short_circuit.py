\"\"\"Micro-Challenge: Guard Clause (Short-Circuiting)
Safe admin check when user might be None.
\"\"\"
user = None  # Try with user = {"access": "admin"} to test

if user and user.get("access") == "admin":
    print("Admin access granted")
else:
    print("Access denied or no user")
