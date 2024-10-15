import random
import string


def generate_password():
    # List and Set Variables for randm_passw print
    password_set = {}  # Update after conditionals
    password_list = []  # Update after conditionals

    # String ASCII & Digit + custom string_speci Variables
    string_upper = string.ascii_uppercase
    string_lower = string.ascii_lowercase
    string_digit = string.digits
    string_speci = ["!", "@", "#", "$", "%", "^", "&", "*"]

    # Random Choice Variables
    upper_chars = random.choice(string_upper)
    speci_chars = random.choice(string_speci)
    lower_chars = ""  # Update on conditional
    numbr_chars = ""  # Update on conditional
    randm_passw = ""  # Update on conditional

    # Random number for conditional
    randm_order = int(random.choice(string_digit))

    # Conditionals for lower_chars, numbr_chars
    for _ in range(0, 3):
        lower_chars += random.choice(string_lower)
    for _ in range(0, 4):
        numbr_chars += random.choice(string_digit)

    if randm_order <= 1:
        password_list = [upper_chars, lower_chars, speci_chars, numbr_chars]
    elif randm_order >= 2 and randm_order <= 4:
        password_list = [upper_chars, lower_chars, numbr_chars, speci_chars]
    elif randm_order >= 5 and randm_order <= 7:
        password_list = [upper_chars, speci_chars, lower_chars, numbr_chars]
    else:
        password_list = [upper_chars, lower_chars, speci_chars, numbr_chars]

    # Conditional for randm_passw
    for _ in range(0, len(password_list)):
        randm_passw += password_list[_]

    # Console print with \n for better readability
    print(f"\nYour generated password is: {randm_passw}\n")
    return randm_passw


generate_password()
