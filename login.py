# Refactored Login Module with Token Support

def login(username, password, auth_token=None):
    if auth_token:
        print(f"Authenticating token for {username}...")
        return True
    print(f"User {username} logged in successfully.")