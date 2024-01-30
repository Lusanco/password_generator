import random
import string


def generate_password():
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

    # Conditionals for lower_chars, numbr_chars, randm_passw
    for _ in range(0, 3):
        lower_chars += random.choice(string_lower)
    for _ in range(0, 4):
        numbr_chars += random.choice(string_digit)

    # Saving generated values, separated in a Set
    password_set = {upper_chars, speci_chars, lower_chars, numbr_chars}

    # Converting generated values, seperated in a List
    password_list = list(password_set)

    for _ in range(0, len(password_list)):
        randm_passw += password_list[_]

    print(randm_passw)
    return randm_passw


generate_password()
