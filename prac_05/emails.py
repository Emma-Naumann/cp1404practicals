"""
Emma Naumann
Practical 5 CP1404
Emails
Estimate: 40 minutes
Actual:
"""


def main():
    """Create dictionary of emails-to-names."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").upper()
        if confirmation != "Y" and confirmation != "":
            name = input("Name: ").title()
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Extract name from email."""
    prefix = email.split("@")[0]
    # parts = prefix.split(".")
    # name = " ".join(parts).title()
    name = prefix.replace(".", " ").title()
    return name


main()
