user = None  

if user is not None and user.get("access") == "admin":
    print("Admin access granted")
else:
    print("Access denied or user is None")
