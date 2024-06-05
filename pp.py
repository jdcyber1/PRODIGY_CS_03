import re

def password_complexity_checker(password):
    errors = []
    if len(password) < 8:
        errors.append("Your password should be at least 8 characters.")
    if not re.search("[a-z]", password):
        errors.append("Your password should have at least one lowercase letter.")
    if not re.search("[A-Z]", password):
        errors.append("Your password should have at least one uppercase letter.")
    if not re.search("[0-9]", password):
        errors.append("Your password should have at least one numeral.")
    if not re.search("[_@$]", password):
        errors.append("Your password should have at least one of the symbols $@_")
    if len(errors) > 2:
        return "Your password is weak. " + ", ".join(errors)
    elif len(errors) > 0:
        return "Your password is moderate. " + ", ".join(errors)
    else:
        return "Your password is strong."

password = input("Enter a password: ")
print(password_complexity_checker(password))