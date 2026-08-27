import re

def is_valid_password(password):
    if len(password)<8:
        return False ,"Password must be 8 Charcter Long "
    if not re.search(r"[A-Z]",password):
        return False, "Password must contain One Uppercase Letter "
    if not re.search(r"[a-z]",password):
        return False, "Password must contain Loweecase Letter "
    if not re.search(r"\d",password):
        return False, 'Password Must Contain One Digit '
    if not re.search(r"[!@#$%^&*<>?]", password):
        return False , "Password Must Contain One Sysmbol "
    
    return True, "Valid Password "


user = input("Enter Your Password :")

valid, message = is_valid_password(user)
print(f"Result: {message}")