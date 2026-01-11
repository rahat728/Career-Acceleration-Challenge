USER = 'guest' # Global user variable

def admin_required(func):
    """
    A decorator that acts as a gatekeeper, allowing only admin users.
    """
    def inner(*args, **kwargs):
        if USER != 'admin':
            print(f"--- [Guard] Access Denied for USER='{USER}' ---")
            raise PermissionError("Access restricted to administrators only.")
        
        print(f"--- [Guard] Access Granted for USER='{USER}' ---")
        return func(*args, **kwargs)
    return inner

@admin_required
def delete_database():
    print("Database deleted successfully! (Just kidding)")

@admin_required
def read_secrets():
    print("Secret key: 12345-ABCDE")

if __name__ == "__main__":
    # Test 1: As Guest (Should fail)
    print(f"Current User: {USER}")
    try:
        read_secrets()
    except PermissionError as e:
        print(f"Caught expected error: {e}")

    print("\n--- Switching to admin... ---")
    USER = 'admin'
    
    # Test 2: As Admin (Should succeed)
    print(f"Current User: {USER}")
    read_secrets()
    delete_database()
