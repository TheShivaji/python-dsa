#Password Length Checker

def check_password(password: str) -> str:

    if len(password) < 8:
        return "Weak Password"


    if password.islower() or password.isupper():
        return "Weak Password: Must contain both upper and lower case letters"


    if not any(char.isdigit() for char in password):
        return "Weak Password: Must contain at least one digit"


    special_chars = "!@#$%^&*(),.?\":{}|<>"
    if not any(char in special_chars for char in password):
        return "Weak Password: Must contain a special character"

    return "Strong Password"

print(check_password("Abc1!xyz"))
print(check_password("12345"))



